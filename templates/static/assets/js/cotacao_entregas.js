// cotacao_entregas.js

function limpa_formulario_cep() {
    // Limpa valores do formulário de cep.
    document.getElementById('rua').value = "";
    document.getElementById('bairro').value = "";
    document.getElementById('cidade').value = "";
    document.getElementById('uf').value = "";

}

function preenche_formulario(conteudo) {
    if (!("erro" in conteudo)) {
        // Atualiza os campos com os valores.
        document.getElementById('rua').value = conteudo.logradouro;
        document.getElementById('bairro').value = conteudo.bairro;
        document.getElementById('cidade').value = conteudo.localidade;
        document.getElementById('uf').value = conteudo.uf;

    } else {
        // CEP não Encontrado.
        limpa_formulario_cep();
        alert("CEP não encontrado.");
    }
}

function pesquisacep(cep) {
    // Nova variável "cep" somente com dígitos.
    cep = cep.replace(/\D/g, '');

    // Verifica se campo cep possui valor informado.
    if (cep !== "") {
        // Expressão regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;

        // Valida o formato do CEP.
        if (validacep.test(cep)) {
            // Preenche os campos com "Carregando..." enquanto consulta o webservice.
            document.getElementById('rua').value = "Carregando...";
            document.getElementById('bairro').value = "Carregando...";
            document.getElementById('cidade').value = "Carregando...";
            document.getElementById('uf').value = "Carregando...";


            // URL da API ViaCEP
            var url = 'https://viacep.com.br/ws/' + cep + '/json/';

            // Requisição AJAX para a API ViaCEP
            var request = new XMLHttpRequest();
            request.open('GET', url);
            request.onreadystatechange = function () {
                if (request.readyState === 4 && request.status === 200) {
                    var response = JSON.parse(request.responseText);
                    preenche_formulario(response);
                } else if (request.status === 400) {
                    limpa_formulario_cep();
                    alert("Formato de CEP inválido.");
                } else if (request.status === 404) {
                    limpa_formulario_cep();
                    alert("CEP não encontrado.");
                }
            };
            request.send();
        } else {
            // CEP é inválido.
            limpa_formulario_cep();
            alert("Formato de CEP inválido.");
        }
    } else {
        // CEP sem valor, limpa formulário.
        limpa_formulario_cep();
    }
}

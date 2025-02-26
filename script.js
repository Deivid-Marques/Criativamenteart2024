document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Impede o envio padrão do formulário

        // Captura os valores do formulário
        const nome = document.querySelector("input[placeholder='Nome completo']").value;
        const email = document.querySelector("input[placeholder='E-mail']").value;
        const senha = document.querySelector("input[placeholder='Senha']").value;

        // Organiza os dados em um objeto
        const dados = {
            nome: nome,
            email: email,
            senha: senha
        };

        // Envia os dados para o Python (servidor local)
        fetch("http://127.0.0.1:5000/salvar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        })
        .then(response => response.json())
        .then(data => {
            alert(data.mensagem); // Exibe uma mensagem de sucesso
            form.reset(); // Limpa o formulário
        })
        .catch(error => console.error("Erro:", error));
    });
});
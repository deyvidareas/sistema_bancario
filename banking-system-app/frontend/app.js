const apiUrl = 'http://localhost:5000';

document.addEventListener('DOMContentLoaded', () => {
    const bankingForm = document.getElementById('banking-form');
    const operationSelect = document.getElementById('operation');
    const amountInput = document.getElementById('amount');
    const amountGroup = document.getElementById('amount-group');
    const output = document.getElementById('message');

    bankingForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const operation = operationSelect.value;
        const amount = parseFloat(amountInput.value);

        if ((operation === 'deposit' || operation === 'withdraw') && (isNaN(amount) || amount <= 0)) {
            output.innerHTML = `<div class="alert alert-danger">Digite um valor válido!</div>`;
            return;
        }

        try {
            let response, result;

            if (operation === 'deposit') {
                response = await fetch(`${apiUrl}/deposit`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ amount })
                });
                result = await response.json();
                output.innerHTML = `<div class="alert alert-success">${result.message}</div>`;

            } else if (operation === 'withdraw') {
                response = await fetch(`${apiUrl}/withdraw`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ amount })
                });
                result = await response.json();
                output.innerHTML = `<div class="alert alert-success">${result.message}</div>`;

            } else if (operation === 'statement') {
                response = await fetch(`${apiUrl}/transactions`);
                result = await response.json();
                const transacoes = result.transactions?.map(t => `<li>${t}</li>`).join('') || "Não foram realizadas movimentações.";
                output.innerHTML = `<div class="alert alert-info">Extrato:<ul>${transacoes}</ul></div>`;
            }

            bankingForm.reset();
        } catch (error) {
            output.innerHTML = `<div class="alert alert-danger">Erro ao realizar operação.</div>`;
            console.error(error);
        }
    });
});
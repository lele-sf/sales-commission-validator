import pytest


@pytest.fixture
def sales_data():
    return [
        {
            "Data da Venda": "2023-11-01",
            "Nome do Vendedor": "João Silva",
            "Valor da Venda": 1000.0,
            "Tipo de Cliente": "Novo",
            "Canal de Venda": "Loja física",
            "Custo da Venda": 100.0,
        },
        {
            "Data da Venda": "2023-11-02",
            "Nome do Vendedor": "Maria Oliveira",
            "Valor da Venda": 500.0,
            "Tipo de Cliente": "Fidelizado",
            "Canal de Venda": "Online",
            "Custo da Venda": 50.0,
        },
        {
            "Data da Venda": "2023-11-03",
            "Nome do Vendedor": "Pedro Souza",
            "Valor da Venda": 2000.0,
            "Tipo de Cliente": "Novo",
            "Canal de Venda": "Telefone",
            "Custo da Venda": 200.0,
        },
    ]


@pytest.fixture
def payment_data():
    return [
        {
            "Data do Pagamento": "2023-12-15",
            "Nome do Vendedor": "João Silva",
            "Comissão": 100.0,
        },
        {
            "Data do Pagamento": "2023-12-15",
            "Nome do Vendedor": "Maria Oliveira",
            "Comissão": 100.0,
        },
        {
            "Data do Pagamento": "2023-12-15",
            "Nome do Vendedor": "Pedro Souza",
            "Comissão": 400.0,
        },
    ]


@pytest.fixture
def client_text():
    return """
    1. João Silva, portador do CPF 123.456.789-00, residente em Rua das Flores, 123, doravante denominado "Sócio 1", detentor de 20 cotas.
    2. Maria Souza, portadora do CPF 987.654.321-00, residente em Avenida dos Anjos, 456, doravante denominada "Sócio 2", detentora de 15 cotas.
    10. Marina Oliveira, portadora do CPF 012.345.678-44, residente em Praça dos Lagos, 456, doravante denominada "Sócio 10", detentora de 1 cota.
    """

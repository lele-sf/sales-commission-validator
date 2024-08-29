import click
from core.handle_data import load_data, save_results, convert_to_dict
from core.calc import calculate_commission
from core.validate import validate_payments
from core.extract_info import extract_client_info


@click.group()
def cli():
    pass


@click.command(name='calculate-commission')
@click.argument("filename")
@click.option("--sheet", default="Vendas", help="Sheet name for sales data")
def calculate_commission_cmd(filename, sheet):
    sales_data = load_data(filename, sheet)
    results = calculate_commission(sales_data)
    headers = ["Nome do Vendedor", "Comissão Inicial", "Comissão Final"]
    save_results(results, headers, "Commissions", "Commissions.xlsx")


@click.command(name='validate-payments')
@click.argument("filename")
@click.option("--sales-sheet", default="Vendas", help="Sheet name for sales data")
@click.option(
    "--payments-sheet", default="Pagamentos", help="Sheet name for payments data"
)
def validate_payments_cmd(filename, sales_sheet, payments_sheet):
    sales_data = load_data(filename, sales_sheet)
    payment_data = load_data(filename, payments_sheet)
    results = validate_payments(sales_data, payment_data)
    headers = ["Nome do Vendedor", "Valor Incorreto", "Valor Correto"]
    save_results(results, headers, "Incorrect Payments", "Incorrect_Payments.xlsx")


@click.command(name='extract-client-info')
@click.argument("filename")
def extract_client_info_cmd(filename):
    client_info = extract_client_info(filename)
    headers = ["Nome do Cliente", "Quantidade de Cotas"]
    client_info_dict = convert_to_dict(client_info, headers)
    save_results(client_info_dict, headers, "Client Info", "Client_Info.xlsx")


cli.add_command(calculate_commission_cmd)
cli.add_command(validate_payments_cmd)
cli.add_command(extract_client_info_cmd)

if __name__ == "__main__":
    cli()

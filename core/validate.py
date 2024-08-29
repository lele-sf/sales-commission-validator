from core.calc import calculate_commission


def validate_payments(sales_data, payment_data):
    try:
        sales_results = calculate_commission(sales_data)
        incorrect_payments = []

        for payment in payment_data:
            seller_name = payment["Nome do Vendedor"]
            paid_commission = payment["Comissão"]
            calculated_commission = 0

            for result in sales_results:
                if result["Nome do Vendedor"] == seller_name:
                    calculated_commission = result["Comissão Final"]
                    break

            if paid_commission != calculated_commission:
                incorrect_payments.append(
                    {
                        "Nome do Vendedor": seller_name,
                        "Valor Incorreto": paid_commission,
                        "Valor Correto": calculated_commission,
                    }
                )

        return incorrect_payments
    except Exception as e:
        print(f"Error validating payments: {e}")
        return []

class LoanCalculator:
    def __init__(self):
        self.monthly_payment_amounts = {}

    def get_monthly_payment(self, principal, interest_rate, loan_term):
        monthly_interest_rate = (interest_rate / 100) / 12
        months_in_loan = loan_term * 12
        monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-months_in_loan))
        self.monthly_payment_amounts[(principal, interest_rate, loan_term)] = round(monthly_payment, 2)
        return monthly_payment

    def monthly_payment(self, principal, interest_rate, loan_term):
        return self.monthly_payment_amounts[(principal, interest_rate, loan_term)]


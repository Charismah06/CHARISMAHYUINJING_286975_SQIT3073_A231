import os
os.system("cls")

def cal_monthly_installment(principal_loan_amount, annual_interest_rate, loan_term_in_years):
    monthly_installment = (principal_loan_amount * (((annual_interest_rate / 100) / 12) * (
                (1 + (annual_interest_rate / 100) / 12) ** (loan_term_in_years * 12))) / (
                                  ((1 + (annual_interest_rate / 100) / 12) ** (loan_term_in_years * 12)) - 1))
    return monthly_installment

def cal_total_payable_loan(monthly_installment, loan_term):
    amount_payable = monthly_installment * (loan_term * 12)
    return amount_payable

def cal_dsr(monthly_installment, monthly_financial_commitments, applicant_monthly_income):
    debt_service_ratio = (monthly_installment + monthly_financial_commitments) / applicant_monthly_income
    return debt_service_ratio

def exit_program():
    print("Exiting the calculator successfully.")
    quit()

debt_service_ratio_range = 0.7
previous_history = []

while True:
    print("\nHousing Loan Eligibility and DSR Calculator:")
    print("~~~~~~Main Menu~~~~~~")
    print("1. Calculate a new loan")
    print("2. Display previous calculations")
    print("3. Delete a previous calculation")
    print("4. Modify Debt Service Ratio (DSR) threshold")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        try:
            principal_loan_amount = float(input("Enter principal amount (RM): "))
            annual_interest_rate = float(input("Enter interest rate: "))
            loan_term_in_years = int(input("Enter loan term (in years): "))
            applicant_monthly_income = float(input("Enter your monthly income (RM): "))
            monthly_financial_commitments = float(input("Enter your monthly financial commitments (RM): "))
        except ValueError:
            print("Invalid input. Please enter valid numerical values.")
            continue
        monthly_installment = cal_monthly_installment(principal_loan_amount, annual_interest_rate, loan_term_in_years)
        total_payable_loan = cal_total_payable_loan(monthly_installment, loan_term_in_years)
        debt_service_ratio = cal_dsr(monthly_installment, monthly_financial_commitments, applicant_monthly_income)
        eligible = "Yes" if debt_service_ratio <= debt_service_ratio_range else "No"
        print("\nLoan Calculation Results:")
        print(f"Monthly Installment: RM {monthly_installment:.2f}")
        print(f"Total Payable Loan: RM {total_payable_loan:.2f}")
        print(f"Debt Service Ratio: {debt_service_ratio:.4%}")
        print(f"Eligible for the loan based on DSR: {eligible}")
        previous_history.append({
            "Principal Loan Amount": principal_loan_amount,
            "Annual Interest Rate": annual_interest_rate,
            "Loan Term (in years)": loan_term_in_years,
            "Monthly Income (RM)": applicant_monthly_income,
            "Monthly Financial Commitments (RM)": monthly_financial_commitments,
            "Monthly Installment": monthly_installment,
            "Total Payable Loan": total_payable_loan,
            "Debt Service Ratio": debt_service_ratio,
            "Eligible or Not Eligible": eligible
        })
    elif choice == '2':
        print("\nPrevious Calculations:")
        for i, entry in enumerate(previous_history):
            print(f"{i + 1}. {entry}")
    elif choice == '3':
        if not previous_history:
            print("No previous calculations to delete.")
        else:
            try:
                index_to_delete = int(input("Enter the index of the calculation to delete: ")) - 1
                del previous_history[index_to_delete]
                print("Calculation deleted successfully.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid index.")
    elif choice == '4':
        try:
            new_dsr_threshold = float(input("Enter the new Debt Service Ratio (DSR) threshold: "))
            debt_service_ratio_range = new_dsr_threshold
            print(f"DSR threshold changed to {new_dsr_threshold:.4%}. Change of DSR successful.")
        except ValueError:
            print("Invalid input. Please enter a valid numerical value for DSR threshold.")
    elif choice == '5':
        exit_program()
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

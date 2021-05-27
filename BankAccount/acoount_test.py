import bankaccount


def main():
    balance = float(input('Введите остаток на счете: '))
    my_account = bankaccount.BankAccount(balance)
    pay = float(input('Внесите зарплату: '))
    print('Вношу деньги на счет...')
    my_account.deposit(pay)
    print('Ваш баланс', my_account.get_balance())
    cash = float(input('Введите сумму, которую хотите снять: '))
    print('Снимаю сумму')
    my_account.withdraw(cash)
    print('Остаток на счет:', my_account.get_balance())


main()

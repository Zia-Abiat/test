
commission_percentage = float(input("commission percentage, between 1 and 100: ")) / 100
original_price = float(input("original price without discount: "))
vendor_discount = float(input("vendor's discount: ")) / 100
company_discount = float(input("company's discount: ")) / 100

gross_receive = original_price - (original_price * vendor_discount)
gross_company_get = gross_receive * commission_percentage
all_discount = vendor_discount + company_discount

user_pay = original_price - (original_price * all_discount)

vendor_get = gross_receive - gross_company_get
print(f"The vendor get: {vendor_get}")

company_get = user_pay - vendor_get
print(f"The company get: {company_get}")


print(user_pay == (vendor_get + company_get))
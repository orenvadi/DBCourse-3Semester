# Import your models
# Import necessary modules
import random

from django.db import transaction
from faker import Faker

from .models import Clients, Goods, OrderInfo, Orders, Pay, Staff, Suppliers

# Create an instance of the Faker class
fake = Faker()


# Function to generate and insert fake data into the database
@transaction.atomic
def populate_database_with_fake_data(num_records):
    for _ in range(num_records):
        # Create Staff instances with fake data
        staff = Staff.objects.create(
            Name=fake.first_name(),
            Surname=fake.last_name(),
            Position=fake.job(),
            InternalPhoneNumber=fake.phone_number(),
            WorkPhoneNumber=fake.phone_number(),
        )

        # Create Suppliers instances with fake data
        supplier = Suppliers.objects.create(
            SupplierOrganizationName=fake.company(),
            Country=fake.country(),
            City=fake.city(),
            PostalCode=fake.zipcode(),
            Adress=fake.street_address(),
            PhoneNumber=fake.phone_number(),
            Fax=fake.phone_number(),
            StandartPayMethod=fake.random_element(
                elements=("Credit Card", "PayPal", "Bank Transfer")
            ),
            StandartBankAccount=fake.iban(),
        )

        # Create Clients instances with fake data
        client = Clients.objects.create(
            CompanyName=fake.company(),
            ContactFullName=fake.name(),
            BillAddress=fake.street_address(),
            City=fake.city(),
            PostalCode=fake.zipcode(),
            Country=fake.country(),
            RecieverJobPosition=fake.job(),
            PhoneNumber=fake.phone_number(),
            Fax=fake.phone_number(),
        )

        # Create Goods instances with fake data
        good = Goods.objects.create(
            SopplierCompanyID=supplier,
            GoodName=fake.word(),
            Producer=fake.company(),
            Price=random.uniform(1.0, 100.0),  # Generate a random price
        )

        # Create Orders instances with fake data
        order = Orders.objects.create(
            ClientID=client,
            StaffWorkerID=staff,
            PostingDate=fake.date_between(start_date="-30d", end_date="today"),
            OrderNUM=fake.unique.random_number(digits=6),
            ReceiverName=fake.name(),
            ReceiverAddress=fake.street_address(),
            ReceiverPostalCode=fake.zipcode(),
            ReceiverPhoneNumber=fake.phone_number(),
            ExecutionDate=fake.date_between(start_date="today", end_date="+30d"),
            DeliveryPrice=random.uniform(5.0, 20.0),  # Generate a random delivery price
            TaxPercentage=random.uniform(
                0.05, 0.15
            ),  # Generate a random tax percentage
        )

        # Create OrderInfo instances with fake data
        order_info = OrderInfo.objects.create(
            OrderID=order,
            GoodID=good,
            Quantity=random.randint(1, 10),  # Generate a random quantity
            Price=good.Price,
            Discount=random.uniform(0.0, 0.2),  # Generate a random discount
        )

        # Create Pay instances with fake data
        pay = Pay.objects.create(
            OrderID=order,
            PayAmount=random.uniform(10.0, 100.0),  # Generate a random payment amount
            PayDate=fake.date_between(start_date="-30d", end_date="today"),
            PayMethod=fake.random_element(
                elements=("Credit Card", "PayPal", "Bank Transfer")
            ),
        )


def fill_db():
    # Create Staff instances
    staff1 = Staff.objects.create(
        Name="John",
        Surname="Doe",
        Position="Manager",
        InternalPhoneNumber="1234",
        WorkPhoneNumber="5678",
    )
    staff2 = Staff.objects.create(
        Name="Jane",
        Surname="Smith",
        Position="Clerk",
        InternalPhoneNumber="4321",
        WorkPhoneNumber="8765",
    )

    # Create Suppliers instances
    supplier1 = Suppliers.objects.create(
        SupplierOrganizationName="Supplier1",
        Country="Country1",
        City="City1",
        PostalCode="12345",
        Adress="Address1",
        PhoneNumber="111-111-1111",
        Fax="111-111-1112",
        StandartPayMethod="PayMethod1",
        StandartBankAccount="BankAccount1",
    )
    supplier2 = Suppliers.objects.create(
        SupplierOrganizationName="Supplier2",
        Country="Country2",
        City="City2",
        PostalCode="54321",
        Adress="Address2",
        PhoneNumber="222-222-2222",
        Fax="222-222-2223",
        StandartPayMethod="PayMethod2",
        StandartBankAccount="BankAccount2",
    )

    # Create Clients instances
    client1 = Clients.objects.create(
        CompanyName="Client1",
        ContactFullName="Contact1",
        BillAddress="BillAddress1",
        City="ClientCity1",
        PostalCode="Client12345",
        Country="ClientCountry1",
        RecieverJobPosition="Manager",
        PhoneNumber="333-333-3333",
        Fax="333-333-3334",
    )
    client2 = Clients.objects.create(
        CompanyName="Client2",
        ContactFullName="Contact2",
        BillAddress="BillAddress2",
        City="ClientCity2",
        PostalCode="Client54321",
        Country="ClientCountry2",
        RecieverJobPosition="Clerk",
        PhoneNumber="444-444-4444",
        Fax="444-444-4445",
    )

    # Create Goods instances
    good1 = Goods.objects.create(
        SopplierCompanyID=supplier1, GoodName="Good1", Producer="Producer1", Price=10.99
    )
    good2 = Goods.objects.create(
        SopplierCompanyID=supplier2, GoodName="Good2", Producer="Producer2", Price=15.99
    )

    # Create Orders instances
    order1 = Orders.objects.create(
        ClientID=client1,
        StaffWorkerID=staff1,
        PostingDate="2023-09-26",
        OrderNUM="Order1",
        ReceiverName="Receiver1",
        ReceiverAddress="ReceiverAddress1",
        ReceiverPostalCode="Receiver12345",
        ReceiverPhoneNumber="555-555-5555",
        ExecutionDate="2023-09-30",
        DeliveryPrice=5.0,
        TaxPercentage=0.08,
    )
    order2 = Orders.objects.create(
        ClientID=client2,
        StaffWorkerID=staff2,
        PostingDate="2023-09-27",
        OrderNUM="Order2",
        ReceiverName="Receiver2",
        ReceiverAddress="ReceiverAddress2",
        ReceiverPostalCode="Receiver54321",
        ReceiverPhoneNumber="666-666-6666",
        ExecutionDate="2023-10-01",
        DeliveryPrice=7.0,
        TaxPercentage=0.1,
    )

    # Create OrderInfo instances
    order_info1 = OrderInfo.objects.create(
        OrderID=order1, GoodID=good1, Quantity=3, Price=10.99, Discount=0.05
    )
    order_info2 = OrderInfo.objects.create(
        OrderID=order2, GoodID=good2, Quantity=5, Price=15.99, Discount=0.1
    )

    # Create Pay instances
    pay1 = Pay.objects.create(
        OrderID=order1, PayAmount=50.0, PayDate="2023-09-26", PayMethod="Credit Card"
    )
    pay2 = Pay.objects.create(
        OrderID=order2, PayAmount=70.0, PayDate="2023-09-27", PayMethod="PayPal"
    )

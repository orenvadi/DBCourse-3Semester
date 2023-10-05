from django.db import models


class Staff(models.Model):
    WorkerID = models.AutoField(primary_key=True)
    Name = models.TextField()
    Surname = models.TextField()
    Position = models.TextField()
    InternalPhoneNumber = models.TextField()
    WorkPhoneNumber = models.TextField()


class Suppliers(models.Model):
    SupplierOrganizationID = models.AutoField(primary_key=True)
    SupplierOrganizationName = models.TextField(unique=True)
    Country = models.TextField()
    City = models.TextField()
    PostalCode = models.TextField()
    Adress = models.TextField()
    PhoneNumber = models.TextField(unique=True)
    Fax = models.TextField(unique=True)
    StandartPayMethod = models.TextField()
    StandartBankAccount = models.TextField(unique=True)


class Clients(models.Model):
    ID = models.AutoField(primary_key=True)
    CompanyName = models.TextField()
    ContactFullName = models.TextField()
    BillAddress = models.TextField()
    City = models.TextField()
    PostalCode = models.TextField()
    Country = models.TextField()
    RecieverJobPosition = models.TextField()
    PhoneNumber = models.TextField()
    Fax = models.TextField()


class Goods(models.Model):
    ID = models.AutoField(primary_key=True)
    SopplierCompanyID = models.ForeignKey(
        Suppliers, on_delete=models.CASCADE, to_field="SupplierOrganizationName"
    )
    GoodName = models.TextField()
    Producer = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)


class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    ClientID = models.ForeignKey(Clients, on_delete=models.CASCADE)
    StaffWorkerID = models.ForeignKey(Staff, on_delete=models.CASCADE)
    PostingDate = models.TextField()
    OrderNUM = models.TextField()
    ReceiverName = models.TextField()
    ReceiverAddress = models.TextField()
    ReceiverPostalCode = models.TextField()
    ReceiverPhoneNumber = models.TextField()
    ExecutionDate = models.TextField()
    DeliveryPrice = models.DecimalField(max_digits=10, decimal_places=2)
    TaxPercentage = models.DecimalField(max_digits=5, decimal_places=2)


class OrderInfo(models.Model):
    ID_of_ordered = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    GoodID = models.ForeignKey(Goods, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Discount = models.DecimalField(max_digits=5, decimal_places=2)


class Pay(models.Model):
    PayID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    PayAmount = models.DecimalField(max_digits=10, decimal_places=2)
    PayDate = models.TextField()
    PayMethod = models.TextField()

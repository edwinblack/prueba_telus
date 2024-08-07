from sqlalchemy import Column, Integer, String, Text, DateTime
from database.database_connection import Base
import datetime


class Summary(Base):
    __tablename__ = 'summary'
    summary_id = Column(Integer, primary_key=True)
    summary_content = Column(Text)
    created_date = Column(DateTime, default=datetime.datetime.now)
    
    def __init__(self,summary_content = None):
        self.summary_content = summary_content

    def __repr__(self):
        return '<Summary>'

class ETL(Base):
    __tablename__ = 'etl'
    summary_id = Column(Integer)
    etl_id = Column(Integer, primary_key=True)
    user_id = Column(Text)
    firstName = Column(Text)
    lastName = Column(Text)
    maidenName = Column(Text)
    age = Column(Text)
    gender = Column(Text)
    email = Column(Text)
    phone = Column(Text)
    username = Column(Text)
    password = Column(Text)
    birthDate = Column(Text)
    image = Column(Text)
    bloodGroup = Column(Text)
    height = Column(Text)
    weight = Column(Text)
    eyeColor = Column(Text)
    ip = Column(Text)
    macAddress = Column(Text)
    university = Column(Text)
    ein = Column(Text)
    ssn = Column(Text)
    userAgent = Column(Text)
    role = Column(Text)
    hair_color = Column(Text)
    hair_type = Column(Text)
    address_address = Column(Text)
    address_city = Column(Text)
    address_state = Column(Text)
    address_stateCode = Column(Text)
    address_postalCode = Column(Text)
    address_coordinates_lat = Column(Text)
    address_coordinates_lng = Column(Text)
    address_country = Column(Text)
    bank_cardExpire = Column(Text)
    bank_cardNumber = Column(Text)
    bank_cardType = Column(Text)
    bank_currency = Column(Text)
    bank_iban = Column(Text)
    company_department = Column(Text)
    company_name = Column(Text)
    company_title = Column(Text)
    company_address_address = Column(Text)
    company_address_city = Column(Text)
    company_address_state = Column(Text)
    company_address_stateCode = Column(Text)
    company_address_postalCode = Column(Text)
    company_address_coordinates_lat = Column(Text)
    company_address_coordinates_lng = Column(Text)
    company_address_country = Column(Text)
    crypto_coin = Column(Text)
    crypto_wallet = Column(Text)
    crypto_network = Column(Text)
    created_date = Column(DateTime, default=datetime.datetime.now)
    
    def __init__(self,
        summary_id = None,
        user_id = None,
        firstName = None,
        lastName = None,
        maidenName = None,
        age = None,
        gender = None,
        email = None,
        phone = None,
        username = None,
        password = None,
        birthDate = None,
        image = None,
        bloodGroup = None,
        height = None,
        weight = None,
        eyeColor = None,
        ip = None,
        macAddress = None,
        university = None,
        ein = None,
        ssn = None,
        userAgent = None,
        role = None,
        hair_color = None,
        hair_type = None,
        address_address = None,
        address_city = None,
        address_state = None,
        address_stateCode = None,
        address_postalCode = None,
        address_coordinates_lat = None,
        address_coordinates_lng = None,
        address_country = None,
        bank_cardExpire = None,
        bank_cardNumber = None,
        bank_cardType = None,
        bank_currency = None,
        bank_iban = None,
        company_department = None,
        company_name = None,
        company_title = None,
        company_address_address = None,
        company_address_city = None,
        company_address_state = None,
        company_address_stateCode = None,
        company_address_postalCode = None,
        company_address_coordinates_lat = None,
        company_address_coordinates_lng = None,
        company_address_country = None,
        crypto_coin = None,
        crypto_wallet = None,
        crypto_network = None
    ):
        self.summary_id = summary_id
        self.user_id = user_id
        self.firstName = firstName
        self.lastName = lastName
        self.maidenName = maidenName
        self.age = age
        self.gender = gender
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password
        self.birthDate = birthDate
        self.image = image
        self.bloodGroup = bloodGroup
        self.height = height
        self.weight = weight
        self.eyeColor = eyeColor
        self.ip = ip
        self.macAddress = macAddress
        self.university = university
        self.ein = ein
        self.ssn = ssn
        self.userAgent = userAgent
        self.role = role
        self.hair_color = hair_color
        self.hair_type = hair_type
        self.address_address = address_address
        self.address_city = address_city
        self.address_state = address_state
        self.address_stateCode = address_stateCode
        self.address_postalCode = address_postalCode
        self.address_coordinates_lat = address_coordinates_lat
        self.address_coordinates_lng = address_coordinates_lng
        self.address_country = address_country
        self.bank_cardExpire = bank_cardExpire
        self.bank_cardNumber = bank_cardNumber
        self.bank_cardType = bank_cardType
        self.bank_currency = bank_currency
        self.bank_iban = bank_iban
        self.company_department = company_department
        self.company_name = company_name
        self.company_title = company_title
        self.company_address_address = company_address_address
        self.company_address_city = company_address_city
        self.company_address_state = company_address_state
        self.company_address_stateCode = company_address_stateCode
        self.company_address_postalCode = company_address_postalCode
        self.company_address_coordinates_lat = company_address_coordinates_lat
        self.company_address_coordinates_lng = company_address_coordinates_lng
        self.company_address_country = company_address_country
        self.crypto_coin = crypto_coin
        self.crypto_wallet = crypto_wallet
        self.crypto_network = crypto_network
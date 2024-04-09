from sqlalchemy import Column, String

from database import Base


class Brand(Base):
    __tablename__ = "brand"

    brand_id = Column(String, primary_key=True)
    generic_id = Column(String)
    company_id = Column(String)
    brand_name = Column(String)
    form = Column(String)
    strength = Column(String)
    price = Column(String)
    packsize = Column(String)


class CompanyName(Base):
    __tablename__ = "company_name"

    company_id = Column(String, primary_key=True)
    company_name = Column(String)
    company_order = Column(String)


class Generic(Base):
    __tablename__ = "generic"

    generic_id = Column(String, primary_key=True)
    generic_name = Column(String)
    precaution = Column(String)
    indication = Column(String)
    contra_indication = Column(String)
    dose = Column(String)
    side_effect = Column(String)
    pregnancy_category_id = Column(String)
    mode_of_action = Column(String)
    interaction = Column(String)


# class Indication(Base):
#     __tablename__ = 'indication'

#     indication_id = Column(String, primary_key=True)
#     indication_name = Column(String)


# class IndicationGenericIndex(Base):
#     __tablename__ = 'indication_generic_index'

#     generic_id = Column(String, primary_key=True)
#     indication_id = Column(String, primary_key=True)


# class PregnancyCategory(Base):
#     __tablename__ = 'pregnancy_category'

#     pregnancy_id = Column(String, primary_key=True)
#     pregnancy_name = Column(String)
#     pregnancy_description = Column(String)


# class Systemic(Base):
#     __tablename__ = 'systemic'

#     systemic_id = Column(String, primary_key=True)
#     systemic_name = Column(String)
#     systemic_parent_id = Column(String)


# class Therapeutic(Base):
#     __tablename__ = 'therapeutic'

#     therapeutic_id = Column(String, primary_key=True)
#     therapeutic_name = Column(String)
#     therapeutic_systemic_class_id = Column(String)


# class TherapeuticGeneric(Base):
#     __tablename__ = 'therapeutic_generic'

#     generic_id = Column(String, primary_key=True)
#     therapeutic_id = Column(String, primary_key=True)

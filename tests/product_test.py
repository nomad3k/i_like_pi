from pi_domain.product import Scope, ScopeType, Product, RelationshipType, Attribute
import json

def test_complex():
    default = (
        Scope(name="default", type=ScopeType.Public)
        .add_attribute("name", Attribute())
        .add_attribute("description", Attribute())
        .add_attribute("purpose", Attribute())
    )
    
    contact_details = (
        Scope(name="contact_details", type=ScopeType.Private)
        .add_attribute("primary_contact", Attribute())
        .add_attribute("primary_contact_email", Attribute())
        .add_attribute("primary_contact_telephone", Attribute())
    )
    
    snomed_codes = (
        Scope(name="snomed_codes", type=ScopeType.Private)
        .add_attribute("snomed_code", Attribute(multiple=True))
    )

    nrl = (
        Product(short_name="NRL", long_name="National Record Locator")
        .add_scope(default)
        .add_scope(contact_details)
        .add_dependency_scope(snomed_codes)
    )

    bars = (
        Product(short_name="BaRS", long_name="Bookings and Referrals Standard API")
        .add_relationship(RelationshipType.DependsUpon, nrl)
    )

    print (nrl.model_dump())
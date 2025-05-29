from django.db import migrations

def copy_lettings_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    # On crée une correspondance entre anciennes et nouvelles adresses
    old_to_new_address_map = {}

    for old_address in OldAddress.objects.all():
        new_address = NewAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )
        old_to_new_address_map[old_address.id] = new_address

    for old_letting in OldLetting.objects.all():
        new_address = old_to_new_address_map.get(old_letting.address_id)
        if new_address:
            NewLetting.objects.create(
                title=old_letting.title,
                address=new_address
            )


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_lettings_data),
    ]
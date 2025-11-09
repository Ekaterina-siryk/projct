import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones_data = list(csv.DictReader(file, delimiter=';'))


        for row in phones_data:
            try:
                id_value = int(row.get('id')),
                name = row.get('name'),
                image =row.get('image'),
                price = int(row.get('price')) if row.get('price') else 0,
                release_date = row.get('release_date'),
                lte_exists = row.get('lte_exists', 'False').lower() == 'true'

                phone, created = Phone.objects.update_or_create(
                    id = id_value,
                    slug = slugify(name),
                    defaults = {
                        'name': name,
                        'image': image,
                        'price': price,
                        'release_date': release_date,
                        'lte_exists': lte_exists,
                    }
                )


                # обновление slug, если название изменилось
                if not phone.slug or phone.slug != slugify(name):
                    phone.slug = slugify(name)
                phone.save()
            except Exception as e:
                self.stderr.write(f'Ошибка при обработке {row.get('name')}: {e}')
        #
        self.stdout.write(self.style.SUCCESS(f'Импортировано {len(phones_data)} телефонов'))


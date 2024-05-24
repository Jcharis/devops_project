import json
from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = """ Import Hospitals json into Django Models 
    usage: 
    python manage.py import_hospitals_data --path hospitals.json
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            type=str,
            help="file path",
            default="ghana_hospitals.json",
        )
    def handle(self, *args, **options):
        file_path = options["path"]
        _model = apps.get_model("hospitals", "Hospital")
        with open(file_path) as f:
            data = json.load(f)
            for hospital in data:
                _model.objects.create(
                    facility_bed=hospital.get('FacilityBed', ''),
                    district=hospital.get('District', ''),
                    hospital_name=hospital.get('Hospital', ''),
                    website=hospital.get('website', ''),
                    city_town=hospital.get('CityTown', ''),
                )
        self.stdout.write(self.style.SUCCESS('Hospitals imported successfully'))
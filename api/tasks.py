import os
import json

from celery import shared_task

from api.models import ScanResult


@shared_task
def scan_target_asynchronously(scan_pk):
    scan = ScanResult.objects.get(pk=scan_pk)
    try:
        # Begin scanning
        os.system(f'trivy image -f json -o {scan.pk}.json {scan.target}')

        # Insert scan result to database
        with open(f'{scan.pk}.json', 'r') as result_file:
            data = json.load(result_file)
            scan.result = data
            scan.status = ScanResult.SUCCESS
            scan.save()

        # Delete scan result file
        os.remove(f'{scan.pk}.json')

    except Exception as e:
        scan.status = ScanResult.FAILED
        scan.has_error = True
        scan.error_message = str(e)
        scan.save()
from django.http import JsonResponse

from .fill import \
    populate_database_with_fake_data as \
    fill_db  # Import your database population script


def populate_database_view(request):
    try:
        fill_db(10)  # Call your database population function
        return JsonResponse({"message": "Database populated successfully"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

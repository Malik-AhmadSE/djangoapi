import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.


# ///////////////// creating the file ///////////////


@csrf_exempt
def create_json_file(request):
    if request.method=='POST':
        filejson=json.loads(request.body)
        botname = filejson['botname']
        print(botname)
        directory='../freq/'
        filename = f'{botname}.json'
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            return JsonResponse({'error': f'A file with the name {filename} already exists in the directory.'})
        with open(filepath, 'w') as f:
            json.dump(filejson, f)
        return JsonResponse({'success':'successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'})
    
    
    
    
# ///////////////// delete the file ////////////////

@csrf_exempt
def delete_file(request):
    if request.method == 'POST':
       filejson=json.loads(request.body)
       botname = filejson['botname']
       print(botname)
       directory='../freq/'
       filename = f'{botname}.json'
       filepath = os.path.join(directory, filename)
       if os.path.exists(filepath):
            os.remove(filename)
            response = {
                'status': 'success',
                'message': f'File {botname}.json deleted successfully.'
            }
            return JsonResponse(response, status=200)
    else:
        response = {
            'status': 'error',
            'message': f'File {botname}.json does not exist.'
        }
        return JsonResponse(response, status=404)

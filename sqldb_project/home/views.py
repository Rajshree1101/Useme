from django.shortcuts import render, redirect
from .models import Inquiry
import logging
from django.db import connections
import openai 
import os

logger = logging.getLogger(__name__)

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def natural_language_to_sql(query):
    prompt = f"""Convert the following natural language query to SQL:
    
Natural language query: {query}

SQL query:"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a SQL expert. Convert natural language queries to SQL."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    sql_query = response.choices[0].message['content'].strip()
    return sql_query

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    return render(request, 'home/contact.html')

def ask_me_anything(request):
    logger.info("ask_me_anything view triggered.")

    if request.method == 'POST':
        employee_name = request.POST.get('employee_name')
        employee_id = request.POST.get('employee_id')
        question = request.POST.get('question')

        logger.info(f"Form data received: {employee_name}, {employee_id}, {question}")

        # Save the inquiry to the database
        inquiry = Inquiry.objects.create(employee_name=employee_name, employee_id=employee_id, question=question)

        logger.info(f"Inquiry object created: {inquiry}")
        
        # Convert natural language question to SQL
        sql_query = natural_language_to_sql(question)
        logger.info(f"Converted SQL query: {sql_query}")

        # Fetch data from 'output_data' database based on the SQL query
        with connections['default'].cursor() as cursor:
            try:
                cursor.execute(sql_query)
                results = cursor.fetchall()
            except Exception as e:
                logger.error(f"Error executing SQL query: {e}")
                results = []

        return render(request, 'home/output.html', {
            'natural_query': question,
            'sql_query': sql_query,
            'results': results
        })

    return render(request, 'home/ask_me_anything.html')

    #     # Fetch data from 'output_data' database based on the question
    #     query = question  # Assuming the question is the SQL query

    #     with connections['default'].cursor() as cursor:
    #         cursor.execute(query)
    #         results = cursor.fetchall()

    #     return render(request, 'home/output.html', {'results': results})

    # return render(request, 'home/ask_me_anything.html')




# # home/views.py
# # home/views.py
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import Inquiry
# import logging

# logger = logging.getLogger(__name__)

# def index(request):
#     return render(request, 'home/index.html')

# def about(request):
#     return render(request, 'home/about.html')

# def services(request):
#     return render(request, 'home/services.html')

# def contact(request):
#     return render(request, 'home/contact.html')

# def ask_me_anything(request):
#     logger.info("ask_me_anything view triggered.")

#     if request.method == 'POST':
#         action = request.POST.get('action')

#         if action == 'submit_inquiry':
#             # Save new inquiry to the database
#             employee_name = request.POST.get('employee_name')
#             employee_id = request.POST.get('employee_id')
#             question = request.POST.get('question')

#             logger.info(f"Form data received: {employee_name}, {employee_id}, {question}")

#             inquiry = Inquiry.objects.create(employee_name=employee_name, employee_id=employee_id, question=question)

#             logger.info(f"Inquiry object created: {inquiry}")

#             # Render success template with inquiry details
#             return render(request, 'home/success.html', {'inquiry': inquiry})

#         elif action == 'submit_query':
#             # Fetch data from 'output_data' database based on the query
#             query = request.POST.get('query')

#             # Example: Use Django ORM to query 'output_data' database
#             # Replace with your actual logic to fetch data from 'output_data'
#             # data = YourModel.objects.using('output_data').filter(some_field=query)

#             # Example data to pass to template
#             results = [{'question': 'Sample Question 1'}, {'question': 'Sample Question 2'}]

#             return render(request, 'home/output.html', {'results': results})

#     # If it's a GET request or form submission failed, render the ask_me_anything.html template
#     return render(request, 'home/ask_me_anything.html')













































# def index(request):
#     return render(request, 'templates/home/index.html')

# def about(request):
#     return render(request, 'templates/home/about.html')

# def services(request):
#     return render(request, 'templates/home/services.html')

# def contact(request):
#     return render(request, 'templates/home/contact.html')


# # Configure logger
# logger = logging.getLogger(__name__)

# def ask_me_anything(request):
#     if request.method == 'POST':
#         # Extract form data
#         employee_name = request.POST.get('employee_name')
#         employee_id = request.POST.get('employee_id')
#         question = request.POST.get('question')

#         # Log form data received
#         logger.info(f"Form data received: {employee_name}, {employee_id}, {question}")

#         # Validate data (optional)
#         if not (employee_name and employee_id and question):
#             logger.error("Form data incomplete. Redirecting back to the form.")
#             return render(request, 'home/ask_me_anything.html', {'error': 'Please fill out all fields.'})

#         # Save the data to the database
#         try:
#             inquiry = Inquiry.objects.create(employee_name=employee_name, employee_id=employee_id, question=question)
#             logger.info(f"Inquiry object created: {inquiry}")
#         except Exception as e:
#             logger.error(f"Error saving inquiry: {e}")
#             return render(request, 'home/ask_me_anything.html', {'error': 'An error occurred. Please try again.'})

#         # Redirect to success page or render success template
#         return render(request, 'home/success.html', {'inquiry': inquiry})

#     # Render the form initially
#     return render(request, 'home/ask_me_anything.html')
# def fetch_data(request):
#     if request.method == 'POST':
#         query = request.POST.get('query')

#         # Assuming you want to fetch data from 'output_data' database
#         with connections['output_data'].cursor() as cursor:
#             cursor.execute(query)
#             data = cursor.fetchall()

#         context = {
#             'query': query,
#             'data': data
#         }
#         return render(request, 'home/fetch_data.html', context)
#     else:
#         return render(request, 'home/ask_me_anything.html')
    
    
    
    
    
    
    

# def index(request):
#     return render(request, 'home/index.html')

# def about(request):
#     return render(request, 'home/about.html')

# def services(request):
#     return render(request, 'home/services.html')

# def contact(request):
#     return render(request, 'home/contact.html')

# def ask_me_anything(request):
#     results = None
#     error = None

#     if request.method == 'POST':
#         action = request.POST.get('action')

#         if action == 'submit_inquiry':
#             # Process inquiry submission
#             employee_name = request.POST.get('employee_name')
#             employee_id = request.POST.get('employee_id')
#             question = request.POST.get('question')

#             # Save to database
#             try:
#                 Inquiry.objects.create(employee_name=employee_name, employee_id=employee_id, question=question)
#                 return render(request, 'home/success.html', {'employee_name': employee_name})  # Replace with your success template
#             except Exception as e:
#                 error = f"An error occurred: {str(e)}"

#         elif action == 'submit_query':
#             # Process query submission
#             query = request.POST.get('query')

#             # Query data from database (replace with your actual query logic)
#             results = Inquiry.objects.filter(question__icontains=query)

#     return render(request, 'home/ask_me_anything.html', {'results': results, 'error': error})

# def fetch_data(request):
#     if request.method == 'POST':
#         query = request.POST.get('query')

#         # Assuming you want to fetch data from 'output_data' database
#         with connections['output_data'].cursor() as cursor:
#             cursor.execute(query)
#             data = cursor.fetchall()

#         context = {
#             'query': query,
#             'data': data
#         }
#         return render(request, 'home/fetch_data.html', context)
#     else:
#         return render(request, 'home/ask_me_anything.html')




# home/views.py
# To save the queries generated by user

# import logging
# logger = logging.getLogger(__name__)

# def ask_me_anything(request):
#     logger.info("ask_me_anything view triggered.")

#     if request.method == 'POST':
#         employee_name = request.POST.get('employee_name')
#         employee_id = request.POST.get('employee_id')
#         question = request.POST.get('question')

#         logger.info(f"Form data received: {employee_name}, {employee_id}, {question}")

#         # Save the data to the database
#         inquiry = Inquiry.objects.create(employee_name=employee_name, employee_id=employee_id, question=question)

#         logger.info(f"Inquiry object created: {inquiry}")

#         # Redirect to success page or render success template
#         return render(request, 'home/success.html', {'inquiry': inquiry})

#     return render(request, 'home/ask_me_anything.html')

# views.py
# To get an output from the database 

# from django.shortcuts import render
# from .models import Inquiry

# def fetch_data(request):
#     if request.method == 'POST':
#         query = request.POST.get('query')
        
#         # Assuming you want to fetch data from 'output_data' database
#         from django.db import connections
        
#         # Using raw SQL query
#         with connections['output_data'].cursor() as cursor:
#             cursor.execute("SELECT * FROM your_table WHERE your_column = %s", [query])
#             data = cursor.fetchall()
        
#         context = {
#             'query': query,
#             'data': data
#         }
#         return render(request, 'home/fetch_data.html', context)
#     else:
#         return render(request, 'home/ask_me_anything.html')






# def ask_me_anything(request):
#     if request.method == 'POST':
#         employee_name = request.POST.get('employee_name')
#         employee_id = request.POST.get('employee_id')
#         question = request.POST.get('question')

#         # Save the data to the database
#         inquiry = Inquiry.objects.create(employee_name=employee_name, employee_id=employee_id, question=question)

#         # Optionally, you can redirect to a success page or render a success message
#         return render(request, 'home/success.html', {'inquiry': inquiry})

#     return render(request, 'home/ask_me_anything.html')


# def ask_me_anything(request):
#     if request.method == 'POST':
#         employee_name = request.POST.get('employee_name')
#         employee_id = request.POST.get('employee_id')
#         question = request.POST.get('question')
#         # Process the form data as needed
#         return HttpResponse(f'Employee Name: {employee_name}, Employee ID: {employee_id}, Question: {question}')
#     return render(request, 'templates/home/ask_me_anything.html')


# Previous code 
# # Create your views here.
# def index(request):
#     # context={"variable":"This is sent"}
#     # return render(request,'index.html',context)
#     return HttpResponse('This is Homepage')
# def about(request):
#     return HttpResponse('This is about page')
# def services(request):
#     return HttpResponse('This is services page')
# def contact(request):
#     return HttpResponse('This is contact page ')
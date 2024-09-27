from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_action(request, action, pk=None):
    if action in ['new', 'edit']:
        employee = Employee.objects.filter(pk=pk).first() if action == 'edit' else None
        form = EmployeeForm(request.POST or None, instance=employee)

        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('employee_list')

        return render(request, 'employees/employee_form.html', {'form': form})

    elif action == 'delete':
        employee = Employee.objects.filter(pk=pk).first()
        if employee is None:
            return redirect('employee_list')

        if request.method == 'POST':
            employee.delete()
            return redirect('employee_list')

        return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

    return redirect('employee_list')

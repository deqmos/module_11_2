from pprint import pprint


class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print('Всего сотрудников: %d' % Employee.empCount)

    def display_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))


def introspection_info(obj):
    info = dict()
    info['type'] = type(obj)
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['methods'] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    info['module'] = getattr(obj, '__module__', 'builtins')
    return info


pprint(introspection_info(42))
print('\n ------------\n')
pprint(introspection_info(Employee))

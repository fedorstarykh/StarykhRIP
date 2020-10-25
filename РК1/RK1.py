# вариант запроса Д
# вариант предметной области 19 : Деталь - Производитель
from operator import itemgetter


class Detail:
    # Деталь
    def __init__(self, id, type, weight, developer_id):
        self.id = id
        self.type = type
        self.weight = weight
        self.developer_id = developer_id


class Developer:
    # Производитель
    def __init__(self, id, name):
        self.id = id
        self.name = name


class DetDev:
    # деталь произовдителя для реализации связи многие-ко-многим
    def __init__(self,  det_id, dev_id):
        self.det_id = det_id
        self.dev_id = dev_id

# Производители
developers = [
    Developer(1, "Venta"),
    Developer(2, "VentPremium"),
    Developer(3, "SanKei"),
    Developer(4, "DetalProm"),
    Developer(5, "DetMos"),
    Developer(6, "DetSPB")
]

# Детали
details = [
    Detail(1, "Motor", 300, 1),
    Detail(2, "Brake disk", 10, 2),
    Detail(3, "Bearing", 1, 2),
    Detail(4, "Machine candles", 1, 3),
    Detail(5, "Headlights", 9, 3),
    Detail(6, "Battery", 15, 3),
    Detail(7, "Exhaust pipes", 18, 4)
]

details_developers = [
    DetDev(1, 1),
    DetDev(2, 2),
    DetDev(2, 3),
    DetDev(3, 4),
    DetDev(3, 5),
    DetDev(3, 6),
    DetDev(4, 7),
    DetDev(4, 1),
    DetDev(5, 2),
    DetDev(5, 3),
    DetDev(5, 4),
    DetDev(5, 5),
    DetDev(6, 6),
    DetDev(6, 7),
]

def main():
    # соединение данных один-ко-многим
    one_to_many = [(dl.type, dl.weight, dr.name)
                   for dr in developers
                   for dl in details
                   if dl.developer_id == dr.id]

    # соединение данных многие-ко-многим

    many_to_many_temp = [(dr.name, dldr.dev_id, dldr.det_id)
                         for dr in developers
                         for dldr in details_developers
                         if dr.id == dldr.dev_id]

    many_to_many = [(dl.type, dl.weight, dev_name)
                    for dev_name, dev_id, det_id in many_to_many_temp
                    for dl in details if dl.id == det_id]

    print('Пункт Д1')
    res1 = []
    for i in one_to_many:
        if i[0][-2:] == "es":
            res1.append(i[0:3:2])
    print(res1)

    print('\nПункт Д2')
    res2_unsorted = []
    for dr in developers:
        dr_details = list(filter(lambda i: i[2] == dr.name, one_to_many))
        if len(dr_details) > 0:
            dr_weight = [listeners for _, listeners, _ in dr_details]
            dr_weight_sum = sum(dr_weight)
            dr_weight_count = len(dr_weight)
            dr_weight_average = dr_weight_sum / dr_weight_count
            res2_unsorted.append((dr.name, int(dr_weight_average)))
    res2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    print(res2)

    print('\nПункт Д3')
    res3 = {}
    for dr in developers:
        if dr.name[0] == "V":
            dr_details = list(filter(lambda i: i[2] == dr.name, many_to_many))
            dr_details_types = [x for x, _, _ in dr_details]
            res3[dr.name] = dr_details_types
    print(res3)


if __name__ == '__main__':
    main()
from API.models import OrderLine, Menu


def get_order_sum(pk):
    sum = 0
    entries = OrderLine.objects.filter(orderid=pk)

    for e in entries:
        item_price = Menu.objects.get(id=e.menuitem.id).price
        amount = e.amount
        sum += (amount * item_price)

    return sum
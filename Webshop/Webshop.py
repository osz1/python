import numpy

# termékek
items = numpy.genfromtxt(
    "raktárkészlet.txt",
    dtype=str,
    delimiter=";",
    skip_header=1,
    usecols=0,
    encoding="utf-8",
)

# árak
prices = numpy.genfromtxt(
    "raktárkészlet.txt",
    dtype=int,
    delimiter=";",
    skip_header=1,
    usecols=1,
    encoding="utf-8",
)

# mennyiségek
quantities = numpy.genfromtxt(
    "raktárkészlet.txt",
    dtype=int,
    delimiter=";",
    skip_header=1,
    usecols=2,
    encoding="utf-8",
)

# rendelés modellezés
month = numpy.arange("2021-11", "2021-12", dtype="datetime64[D]")
for day in month:
    date = str(day).replace("-", ".")
    random_item = numpy.random.choice(items)
    random_quantity = numpy.random.randint(1, 15)

    idx = numpy.where(items == random_item)

    random_pay = random_quantity * prices[idx][0]

    line = (
        "\n"
        + random_item
        + ";"
        + str(random_quantity)
        + ";"
        + str(random_pay)
        + ";"
        + date
    )

    if random_quantity <= quantities[idx]:
        with open("rendelések.txt", "a", encoding="utf-8") as file:
            file.write(line + ";igen")

        quantities[idx] -= random_quantity

        numpy.savetxt(
            "raktárkészlet.txt",
            numpy.stack((items, prices, quantities), axis=-1),
            fmt="%s",
            delimiter=";",
            header="TERMÉK_NEVE|TERMÉK_ÁRA|RENDELKEZÉSRE_ÁLLÓ_MENNYISÉG",
            encoding="utf-8",
        )
    else:
        with open("rendelések.txt", "a", encoding="utf-8") as file:
            file.write(line + ";nem")

# rendelés statisztika
order_item = numpy.genfromtxt(
    "rendelések.txt",
    dtype=str,
    delimiter=";",
    skip_header=1,
    usecols=0,
    encoding="utf-8",
)
order_quantity = numpy.genfromtxt(
    "rendelések.txt",
    dtype=int,
    delimiter=";",
    skip_header=1,
    usecols=1,
    encoding="utf-8",
)
order_pay = numpy.genfromtxt(
    "rendelések.txt",
    dtype=int,
    delimiter=";",
    skip_header=1,
    usecols=2,
    encoding="utf-8",
)
order_date = numpy.genfromtxt(
    "rendelések.txt",
    dtype=str,
    delimiter=";",
    skip_header=1,
    usecols=3,
    encoding="utf-8",
)
order_successfulness = numpy.genfromtxt(
    "rendelések.txt",
    dtype=str,
    delimiter=";",
    skip_header=1,
    usecols=4,
    encoding="utf-8",
)

order_item_uniq = numpy.unique(order_item)
success_order_quantity = numpy.zeros(len(order_item_uniq))
success_order_pay = numpy.zeros(len(order_item_uniq))

success = 0
unsuccess = 0
for idx, x in numpy.ndenumerate(order_item):
    if order_successfulness[idx] == "igen":
        success_order_quantity[numpy.where(order_item_uniq == x)] += order_quantity[idx]
        success_order_pay[numpy.where(order_item_uniq == x)] += order_pay[idx]
        success += 1
    else:
        unsuccess += 1

print(
    "melyik termékből hány darab került eladásra\n",
    numpy.stack((order_item_uniq, success_order_quantity), axis=-1),
)
print(
    "melyik termékből mennyi maradt raktáron a hónap végére\n",
    numpy.genfromtxt(
        "raktárkészlet.txt",
        dtype=str,
        delimiter=";",
        skip_header=1,
        usecols=(0, -1),
        encoding="utf-8",
    ),
)
print(
    "mi volt a legnépszerűbb termék a hónapban",
    order_item_uniq[numpy.where(success_order_quantity == max(success_order_quantity))],
)
print(
    "melyik termék mennyi bevételt hozott a webshopnak a hónapban\n",
    numpy.stack((order_item_uniq, success_order_pay), axis=-1),
)
print("mennyi volt a webshop teljes bevétele a hónapban", numpy.sum(order_pay))
print("hány sikeres és hány sikertelen rendelés végrehajtás volt összesen")
print("sikeres", success, "\nsikertelen", unsuccess)
print(
    "melyik napon történt a legtöbb megrendelés",
    order_date[numpy.where(order_quantity == max(order_quantity))],
)

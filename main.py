import asyncio


async def sow_plant(name, soak_time, grow_time, settle_time):
    print(f"0 Beginning of sowing the {name} plant")

    print(f"1 Soaking of the {name} started")
    await asyncio.sleep(soak_time / 1000)
    print(f"2 Soaking of the {name} is finished")

    print(f"3 Shelter of the {name} is supplied")
    await asyncio.sleep(grow_time / 1000)

    print(f"4 Shelter of the {name} is removed")
    print(f"5 The {name} has been transplanted")
    await asyncio.sleep(settle_time / 1000)

    print(f"6 The {name} has taken root")
    print(f"9 The seedlings of the {name} are ready")


async def fertilize(name):
    print(f"7 Application of fertilizers for {name}")
    await asyncio.sleep(3 / 1000)
    print(f"7 Fertilizers for the {name} have been introduced")


async def treat_pests(name):
    print(f"8 Treatment of {name} from pests")
    await asyncio.sleep(5 / 1000)
    print(f"8 The {name} is treated from pests")


async def sowing(*plants):
    tasks = []
    for name, soak, grow, settle in plants:
        tasks.append(asyncio.create_task(sow_plant(name, soak, grow, settle)))
        tasks.append(asyncio.create_task(fertilize(name)))
        tasks.append(asyncio.create_task(treat_pests(name)))

    await asyncio.gather(*tasks)

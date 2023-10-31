import psutil


def list_logical_drives_info():
    partitions = psutil.disk_partitions(all=False)

    for partition in partitions:
        drive = partition.device
        mountpoint = partition.mountpoint
        fstype = partition.fstype
        try:
            usage = psutil.disk_usage(mountpoint)
            label = psutil.disk_partitions(all=True)[partitions.index(partition)].opts.split('label=')[1] if 'label=' in \
                                                                                                             psutil.disk_partitions(
                                                                                                                 all=True)[
                                                                                                                 partitions.index(
                                                                                                                     partition)].opts else 'Нет'
            print(f"Диск: {drive}")
            print(f"Метка тома: {label}")
            print(f"Размер диска: {usage.total / (1024 ** 3):.2f} ГБ")
            print(f"Свободное место: {usage.free / (1024 ** 3):.2f} ГБ")
            print(f"Тип файловой системы: {fstype}")
            print()
        except Exception as e:
            print(f"Ошибка при получении информации о диске {drive}: {str(e)}")


list_logical_drives_info()

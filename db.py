import psycopg2


def connection_db():  # SQL
    conn = psycopg2.connect(
        database='test_db',
        user='admin',
        password='docker',
        host="127.0.0.1",
        port="54320")
    return conn


def insert_building_info(con, street, building_no, building_corps, construction_no, device_no):
    cur = con.cursor()
    test_ins = """insert into buildings (street, building_no, building_corps, construction_no, device_no)
                                            values(%s, %s, %s, %s, %s);"""

    cur.execute(test_ins, (street, building_no, building_corps, construction_no, device_no,))

    con.commit()


def insert_stock_info(con, tariff, coefficient, mount_place, device_no, date_of_mount, date_check, transform_coeff,
                      type_current, no_phase_a, no_phase_b, no_phase_c):
    cur = con.cursor()
    test_ins = """insert into stock_info (tariff, coefficient, mount_place, device_no, date_of_mount, date_check,
                                            transform_coeff, type_current, no_phase_a, no_phase_b , no_phase_c)
                                            values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    cur.execute(test_ins, (tariff, coefficient, mount_place, device_no, date_of_mount, date_check,
                           transform_coeff, type_current, no_phase_a, no_phase_b, no_phase_c))
    con.commit()


def create_tables(con):
    cur = con.cursor()
    # tariff =Тарифность
    # coefficient = Расчетный коэффициент
    # mount_place = Место установки существующего ПУ
    # device_no = Заводской номер существующего прибора учета PK
    # date_of_mount = Дата установки существующего прибора учета
    # date_check = Дата следующей поверки
    # transform_coeff = Коэффициент трансформации
    # type_current = Тип трансформатора тока
    # no_phase_a = Номер ТТ фаза А
    # no_phase_b = Номер ТТ фаза B
    # no_phase_c = Номер ТТ фаза C
    table_stock_into = """create table stock_info(
                                            id_stock       serial REFERENCES buildings (id_building),
                                            tariff          varchar(10),
                                            coefficient     varchar(10),
                                            mount_place     varchar(100),
                                            device_no       varchar(100),
                                            date_of_mount   date,
                                            date_check      date,
                                            transform_coeff varchar(20),
                                            type_current    varchar(20),
                                            no_phase_a      varchar(10),
                                            no_phase_b      varchar(10),
                                            no_phase_c      varchar(10)
                                            );"""

    # street =Улица
    # building_no = № дома
    # building_corps = Корпус
    # construction_no = Строение
    # device_no = Заводской номер существующего прибора учета
    table_buildings = """create table buildings(
                                        id_building     serial PRIMARY KEY,
                                        street          varchar(200),
                                        building_no     varchar(50),
                                        building_corps  varchar(5),
                                        construction_no varchar (5),
                                        device_no       varchar(100)
                                        );"""

    cur.execute(table_buildings)
    cur.execute(table_stock_into)
    con.commit()

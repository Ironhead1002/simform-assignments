PGDMP     3                    y            practice    10.19    10.19     ?
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            ?
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            ?
           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            ?
           1262    16393    practice    DATABASE     ?   CREATE DATABASE practice WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_India.1252' LC_CTYPE = 'English_India.1252';
    DROP DATABASE practice;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            ?
           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12924    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            ?
           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            ?            1259    16394    employeeinfo    TABLE       CREATE TABLE public.employeeinfo (
    empid integer NOT NULL,
    empfname character varying(30),
    emplname character varying(30),
    department character varying(20),
    project character varying(20),
    address character varying(20),
    dob date,
    gender character(1),
    CONSTRAINT employeeinfo_gender_check CHECK ((gender = ANY (ARRAY['M'::bpchar, 'F'::bpchar])))
);
     DROP TABLE public.employeeinfo;
       public         postgres    false    3            ?            1259    16406    employeeposition    TABLE     ?   CREATE TABLE public.employeeposition (
    empid integer,
    empposition character varying(30),
    dateofjoining date,
    salary integer
);
 $   DROP TABLE public.employeeposition;
       public         postgres    false    3            ?
          0    16394    employeeinfo 
   TABLE DATA               l   COPY public.employeeinfo (empid, empfname, emplname, department, project, address, dob, gender) FROM stdin;
    public       postgres    false    196          ?
          0    16406    employeeposition 
   TABLE DATA               U   COPY public.employeeposition (empid, empposition, dateofjoining, salary) FROM stdin;
    public       postgres    false    197   ?       r
           2606    16399    employeeinfo employeeinfo_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.employeeinfo
    ADD CONSTRAINT employeeinfo_pkey PRIMARY KEY (empid);
 H   ALTER TABLE ONLY public.employeeinfo DROP CONSTRAINT employeeinfo_pkey;
       public         postgres    false    196            s
           2606    16409    employeeposition fk_empid    FK CONSTRAINT     ?   ALTER TABLE ONLY public.employeeposition
    ADD CONSTRAINT fk_empid FOREIGN KEY (empid) REFERENCES public.employeeinfo(empid);
 C   ALTER TABLE ONLY public.employeeposition DROP CONSTRAINT fk_empid;
       public       postgres    false    197    2674    196            ?
   ?   x?u????0E׷_??N?*K&h0??٘??)$T?51??E'???y?{?9ObG?DtU??|?B"ʪ??A??&??<?Rq!??Bj?mnc#-/ƢPȪ?6A?،?(?"?Baɦغ?,2s?7=]o;S??r |~????B̰s??}s?֚wV??????l:???\?F*?q1?Y????Ԯ?o???????>cXTN{      ?
   S   x?3??M?KLO-?4202?50?50?45 .#N׊??Ғ̲T???9H???FK?>N???d-`-???3?4?????? 6?k     
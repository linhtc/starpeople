Work Activity
=============

Tài liệu này mô tả cách các phần liên quan đến Quản lý công việc. Bao gồm:

* :ref:`in-work-timekeeping`
* :ref:`in-work-absent`
* :ref:`in-work-overtime`

.. _in-work-timekeeping:

Timekeeping activity
--------------------


Check-In
~~~~~~~~~~~

.. http:post::  /api/v1/works/timekeeping/checkin

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.
   :arg location: (lat,long) Kinh độ, vĩ độ thực hiện chấm công vào.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "fullname": "[10.785092,106.6913373]"
      }


   :>json boolean status: Trạng thái xử lý của Server.
   :>json string status: Thời gian Server ghi nhận ("Y-m-d H:i:s").


Check-Out
~~~~~~~~~~~

.. http:post::  /api/v1/works/timekeeping/checkout

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.
   :arg location: (lat,long) Kinh độ, vĩ độ thực hiện chấm công ra.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "fullname": "[10.785092,106.6913373]"
      }


   :>json boolean status: Trạng thái xử lý của Server.
   :>json string written_time: Thời gian Server ghi nhận ("Y-m-d H:i:s").
   
.. _in-work-absent:

Absent activity
---------------


Apply for absence
~~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/apply

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.
   :arg start_time: Thời gian bắt đầu.
   :arg end_time: Thời gian kết thúc.
   :arg reason: Lý do nghỉ phép.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "start_time": "2017-08-14 08:00",
          "end_time": "2017-08-15 08:00",
          "reason": "Bệnh rất nặng :(("
      }


   :>json boolean status: Trạng thái xử lý của Server.


Absence approval
~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/confirm

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.
   :arg absence_id: ID của đơn xin phép.
   :arg approval: Đồng ý hay từ chối (1/0).
   :arg message: Lời nhắn đến người gửi đơn.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "absence_id": "19863",
          "approval": "0",
          "message": "Nghỉ luôn thì được ^_^"
      }


   :>json boolean status: Trạng thái xử lý của Server.


Absence table
~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/table

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.

   .. sourcecode:: js

      {
          "access_token": "_HASH_"
      }


   :>json boolean status: Trạng thái xử lý của Server.
   :>json array list: Danh sách các `Absence detail`_ object..


Absence detail
~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/detail

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.
   :arg absence_id: ID của đơn xin phép.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "absence_id": "18963",
      }


   :>json boolean status: Trạng thái xử lý của Server.
   :>json string fullname: Người nộp đơn.
   :>json string absent_time: Thời gian nghỉ [start to end].
   :>json string reason: Lý do nghỉ.
   
.. _in-work-overtime:

Overtime activity
-----------------


Apply for OT
~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/apply

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.
   :arg start_time: Thời gian bắt đầu.
   :arg end_time: Thời gian kết thúc.
   :arg reason: Lý do tăng ca.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "start_time": "2017-08-14 08:00",
          "end_time": "2017-08-15 08:00",
          "reason": "ItViec - Ít mà chất nên làm chậm deadline ;(("
      }


   :>json boolean status: Trạng thái xử lý của Server.


Overtime approval
~~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/confirm

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.
   :arg overtime_id: ID của đơn yêu cầu tăng ca.
   :arg approval: Đồng ý hay từ chối (1/0).
   :arg message: Lời nhắn đến người gửi đơn.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "overtime_id": "19863",
          "approval": "0",
          "message": "Người ta làm 5' còn em là 1 tuần là như nào?"
      }


   :>json boolean status: Trạng thái xử lý của Server.


Overtime table
~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/table

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.

   .. sourcecode:: js

      {
          "access_token": "_HASH_"
      }


   :>json boolean status: Trạng thái xử lý của Server.
   :>json array list: Danh sách các `Overtime detail`_ object..


Overtime detail
~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/detail

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.
   :arg overtime_id: ID của đơn yêu cầu.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "overtime_id": "18963",
      }


   :>json boolean status: Trạng thái xử lý của Server.
   :>json string fullname: Người nộp đơn.
   :>json string absent_time: Thời gian yêu cầu tính tăng ca [start to end].
   :>json string reason: Lý do yêu cầu.

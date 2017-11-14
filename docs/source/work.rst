Work Activities
===============

Tài liệu này mô tả các phần liên quan đến Quản lý công việc. Bao gồm:

* :ref:`in-work-timekeeping`
* :ref:`in-work-absent`
* :ref:`in-work-overtime`

.. _in-work-timekeeping:

Timekeeping activity
--------------------


Check-In
~~~~~~~~

.. http:post::  /api/v1/works/timekeeping/checkin

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg location: [lat,long] Kinh độ, vĩ độ thực hiện chấm công vào.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "location": [10.785092,106.6913373]
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json long written_time: Thời gian Server ghi nhận (Unix timestamp).

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "written_time": 1513651191000
      }


Check-Out
~~~~~~~~~

.. http:post::  /api/v1/works/timekeeping/checkout

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg location: [lat,long] Kinh độ, vĩ độ thực hiện chấm công ra.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "location": [10.785092,106.6913373]
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json long written_time: Thời gian Server ghi nhận (Unix timestamp).

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "written_time": 1513651191000
      }


.. _in-work-absent:

Absent activity
---------------


Apply for absence
~~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/apply

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg start_time: Thời gian bắt đầu.
   :arg end_time: Thời gian kết thúc.
   :arg kind: Loại phép (Xem :ref:`in-rule-kind-mapping`).
   :arg reason: Lý do nghỉ.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "start_time": "2017-08-14 08:00",
          "end_time": "2017-08-15 08:00",
          "kind": 0,
          "reason": "Bệnh rất nặng :(("
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": ""
      }


Absence approval
~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/confirm

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg absence_id: ID của đơn xin phép.
   :arg approval: Phê duyệt (Xem :ref:`in-rule-approval-mapping`).
   :arg message: Lời nhắn đến người gửi đơn.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "absence_id": "19863",
          "approval": 0,
          "message": "Nghỉ luôn thì được ^_^"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": ""
      }


Absence table
~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/table

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "user_id": "18963",
          "client_id": "18963"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json array data: Danh sách các `Absence detail`_ object..

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "data": [{
             "absence_id": "19863",
             "user_id": "18963",
             "fullname": "Leon Tran",
             "position": "DEV",
             "deparment": "VAS",
             "branch": "HCM",
             "phone": "0961095661",
             "email": "leon.tran@mobistar.vn",
             "absent_time": [1513651191000, 1513651191000],
             "kind": 0,
             "reason": "Bệnh"
          }]
      }


.. _in-work-absence-detail:

Absence detail
~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/detail

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg absence_id: ID của đơn xin phép.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "absence_id": "18963"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json object data: :ref:`in-rule-data-absent`.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "data":
          {
             "absence_id": "19863",
             "user_id": "18963",
             "fullname": "Leon Tran",
             "position": "DEV",
             "deparment": "VAS",
             "branch": "HCM",
             "phone": "0961095661",
             "email": "leon.tran@mobistar.vn",
             "absent_time": [1513651191000, 1513651191000],
             "kind": 0,
             "reason": "Bệnh"
          }
      }


Absence management
~~~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/management

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg user_id: ID người dùng (quản lý hoặc nhân viên).
   :arg client_id: ID client.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "user_id": "18963",
          "client_id": "18963"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json integer remain: Số ngày phép còn lại.
   :>json integer total: Tất cả đơn đã nhận/ gửi.
   :>json integer waiting_for_approval: Số đơn chờ duyệt.
   :>json integer total_approval: Số đơn đã/ đã được duyệt.
   :>json integer total_unapproved: Số đơn không/ không được duyệt.
   :>json integer total_update: Số đơn yêu cầu/ được yêu cầu chỉnh sửa.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "remain": 10,
          "total": 10,
          "waiting_for_approval": 10,
          "total_approval": 10,
          "total_unapproved": 10,
          "total_update": 10
      }


.. _in-work-overtime:

Overtime activity
-----------------


Apply for OT
~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/apply

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg start_time: Thời gian bắt đầu.
   :arg end_time: Thời gian kết thúc.
   :arg reason: Lý do tăng ca.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "start_time": "2017-08-14 08:00",
          "end_time": "2017-08-15 08:00",
          "reason": "ItViec - Ít mà chất nên làm chậm deadline ;(("
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": ""
      }


Overtime approval
~~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/confirm

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg overtime_id: ID của đơn yêu cầu tăng ca.
   :arg approval: Phê duyệt (Xem :ref:`in-rule-approval-mapping`).
   :arg message: Lời nhắn đến người gửi đơn.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "overtime_id": "19863",
          "approval": 0,
          "message": "Người ta làm 5' còn em là 1 tuần là như nào?"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": ""
      }


Overtime table
~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/table

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json array data: Danh sách các `Overtime detail`_ object..

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "data": [{
             "overtime_id": "19863",
             "user_id": "18963",
             "fullname": "Leon Tran",
             "position": "DEV",
             "deparment": "VAS",
             "branch": "HCM",
             "phone": "0961095661",
             "email": "leon.tran@mobistar.vn",
             "absent_time": [1513651191000, 1513651191000],
             "reason": "Urgent"
          }]
      }


.. _in-work-overtime-detail:

Overtime detail
~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/detail

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg overtime_id: ID của đơn yêu cầu.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "overtime_id": "18963",
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json object data: :ref:`in-rule-data-overtime`.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "data":
          {
             "overtime_id": "19863",
             "user_id": "18963",
             "fullname": "Leon Tran",
             "position": "DEV",
             "deparment": "VAS",
             "branch": "HCM",
             "phone": "0961095661",
             "email": "leon.tran@mobistar.vn",
             "absent_time": [1513651191000, 1513651191000],
             "reason": "Urgent"
          }
      }


Overtime management
~~~~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/management

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg user_id: ID người dùng (quản lý hoặc nhân viên).
   :arg client_id: ID client.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "user_id": "18963",
          "client_id": "18963"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json integer total: Tất cả đơn đã nhận/ gửi.
   :>json integer waiting_for_approval: Số đơn chờ duyệt.
   :>json integer total_approval: Số đơn đã/ đã được duyệt.
   :>json integer total_unapproved: Số đơn không/ không được duyệt.
   :>json integer total_update: Số đơn yêu cầu/ được yêu cầu chỉnh sửa.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "total": 10,
          "waiting_for_approval": 10,
          "total_approval": 10,
          "total_unapproved": 10,
          "total_update": 10
      }

   

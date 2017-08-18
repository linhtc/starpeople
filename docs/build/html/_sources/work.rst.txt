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
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg location: [lat,long] Kinh độ, vĩ độ thực hiện chấm công vào.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "location": [10.785092,106.6913373]
      }


   :>json boolean status: :ref:`in-rule-res-status`.
   :>json string written_time: Thời gian Server ghi nhận ("Y-m-d H:i:s").

   .. sourcecode:: js

      {
          "status": true,
          "written_time": "2017-07-17 07:59:00" 
      }


Check-Out
~~~~~~~~~

.. http:post::  /api/v1/works/timekeeping/checkout

   :arg access_token: Xem :ref:`in-get-token`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg location: [lat,long] Kinh độ, vĩ độ thực hiện chấm công ra.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "location": [10.785092,106.6913373]
      }


   :>json boolean status: :ref:`in-rule-res-status`.
   :>json string written_time: Thời gian Server ghi nhận ("Y-m-d H:i:s").

   .. sourcecode:: js

      {
          "status": true,
          "written_time": "2017-07-17 17:31:00" 
      }


.. _in-work-absent:

Absent activity
---------------


Apply for absence
~~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/apply

   :arg access_token: Xem :ref:`in-get-token`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg start_time: Thời gian bắt đầu.
   :arg end_time: Thời gian kết thúc.
   :arg kind: Loại phép (Xem :ref:`in-rule-kind-mapping`).
   :arg reason: Lý do nghỉ.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "start_time": "2017-08-14 08:00",
          "end_time": "2017-08-15 08:00",
          "kind": 0,
          "reason": "Bệnh rất nặng :(("
      }


   :>json boolean status: :ref:`in-rule-res-status`.

   .. sourcecode:: js

      {
          "status": true
      }


Absence approval
~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/confirm

   :arg access_token: Xem :ref:`in-get-token`.
   :arg absence_id: ID của đơn xin phép.
   :arg approval: Phê duyệt (Xem :ref:`in-rule-approval-mapping`).
   :arg message: Lời nhắn đến người gửi đơn.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "absence_id": "19863",
          "approval": 0,
          "message": "Nghỉ luôn thì được ^_^"
      }


   :>json boolean status: :ref:`in-rule-res-status`.

   .. sourcecode:: js

      {
          "status": true
      }


Absence table
~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/table

   :arg access_token: Xem :ref:`in-get-token`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "user_id": "18963",
          "client_id": "18963"
      }


   :>json boolean status: :ref:`in-rule-res-status`.
   :>json array list: Danh sách các `Absence detail`_ object..

   .. sourcecode:: js

      {
          "status": true,
          "list": [{
          	"absence_id": "18963",
          	"fullname": "Leon Tran",
          	"absent_time": "2017-07-17 08:00:00 -> 2017-07-18 08:00:00",
          	"kind": 0,
          	"reason": "Bệnh"
          }]
      }


Absence detail
~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/detail

   :arg access_token: Xem :ref:`in-get-token`.
   :arg absence_id: ID của đơn xin phép.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "absence_id": "18963",
      }


   :>json boolean status: :ref:`in-rule-res-status`.
   :>json string fullname: Người nộp đơn.
   :>json string absent_time: Thời gian nghỉ [start to end].
   :>json integer kind: Loại phép (Xem :ref:`in-rule-kind-mapping`).
   :>json string reason: Lý do nghỉ.

   .. sourcecode:: js

      {
          "status": true,
          "fullname": "Leon Tran",
          "absent_time": "2017-07-17 08:00:00 -> 2017-07-18 08:00:00",
          "kind": 0,
          "reason": "Bệnh"
      }


Absence management
~~~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/absent/management

   :arg access_token: Xem :ref:`in-get-token`.
   :arg user_id: ID người dùng (quản lý hoặc nhân viên).
   :arg client_id: ID client.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "user_id": "18963",
          "client_id": "18963"
      }


   :>json boolean status: :ref:`in-rule-res-status`.
   :>json integer remain: Số ngày phép còn lại.
   :>json integer total: Tất cả đơn đã nhận/ gửi.
   :>json integer waiting_for_approval: Số đơn chờ duyệt.
   :>json integer total_approval: Số đơn đã/ đã được duyệt.
   :>json integer total_unapproved: Số đơn không/ không được duyệt.
   :>json integer total_update: Số đơn yêu cầu/ được yêu cầu chỉnh sửa.

   .. sourcecode:: js

      {
          "status": true,
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
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg start_time: Thời gian bắt đầu.
   :arg end_time: Thời gian kết thúc.
   :arg reason: Lý do tăng ca.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "start_time": "2017-08-14 08:00",
          "end_time": "2017-08-15 08:00",
          "reason": "ItViec - Ít mà chất nên làm chậm deadline ;(("
      }


   :>json boolean status: :ref:`in-rule-res-status`.

   .. sourcecode:: js

      {
          "status": true
      }


Overtime approval
~~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/confirm

   :arg access_token: Xem :ref:`in-get-token`.
   :arg overtime_id: ID của đơn yêu cầu tăng ca.
   :arg approval: Phê duyệt (Xem :ref:`in-rule-approval-mapping`).
   :arg message: Lời nhắn đến người gửi đơn.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "overtime_id": "19863",
          "approval": 0,
          "message": "Người ta làm 5' còn em là 1 tuần là như nào?"
      }


   :>json boolean status: :ref:`in-rule-res-status`.

   .. sourcecode:: js

      {
          "status": true
      }


Overtime table
~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/table

   :arg access_token: Xem :ref:`in-get-token`.

   .. sourcecode:: js

      {
          "access_token": "_HASH_"
      }


   :>json boolean status: :ref:`in-rule-res-status`.
   :>json array list: Danh sách các `Overtime detail`_ object..

   .. sourcecode:: js

      {
          "status": true,
          "list": [{
          	"overtime_id": "18963",
          	"fullname": "Leon Tran",
          	"absent_time": "2017-07-17 08:00:00 -> 2017-07-18 08:00:00",
          	"reason": "Urgent"
          }]
      }


Overtime detail
~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/detail

   :arg access_token: Xem :ref:`in-get-token`.
   :arg overtime_id: ID của đơn yêu cầu.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "overtime_id": "18963",
      }


   :>json boolean status: :ref:`in-rule-res-status`.
   :>json string fullname: Người nộp đơn.
   :>json string overtime_time: Thời gian yêu cầu tính tăng ca [start to end].
   :>json string reason: Lý do yêu cầu.

   .. sourcecode:: js

      {
          "status": true,
          "fullname": "Leon Tran",
          "overtime_time": "2017-07-17 08:00:00 -> 2017-07-18 08:00:00",
          "reason": "Urgent"
      }


Overtime management
~~~~~~~~~~~~~~~~~~~

.. http:post::  /api/v1/works/overtime/management

   :arg access_token: Xem :ref:`in-get-token`.
   :arg user_id: ID người dùng (quản lý hoặc nhân viên).
   :arg client_id: ID client.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "user_id": "18963",
          "client_id": "18963"
      }


   :>json boolean status: :ref:`in-rule-res-status`.
   :>json integer total: Tất cả đơn đã nhận/ gửi.
   :>json integer waiting_for_approval: Số đơn chờ duyệt.
   :>json integer total_approval: Số đơn đã/ đã được duyệt.
   :>json integer total_unapproved: Số đơn không/ không được duyệt.
   :>json integer total_update: Số đơn yêu cầu/ được yêu cầu chỉnh sửa.

   .. sourcecode:: js

      {
          "status": true,
          "total": 10,
          "waiting_for_approval": 10,
          "total_approval": 10,
          "total_unapproved": 10,
          "total_update": 10
      }

   

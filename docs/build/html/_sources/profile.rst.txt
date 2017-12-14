Employee Profile
================

Tài liệu này mô tả cách sử dụng thông tin người dùng từ WebService. Bao gồm các phần sau:

* :ref:`in-profile-get`
* :ref:`in-profile-update`
* :ref:`in-profile-permission`
* :ref:`in-profile-shift`

.. _in-profile-get:

Get profile
-----------
.. http:post::  /api/v1/profile/get

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
   :>json object data: :ref:`in-rule-data-profile`.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "data":
          {
             "access_code": "_HASH_",
             "user_id": "18963",
             "fullname": "Leon Tran",
             "position": "DEV",
             "deparment": "VAS",
             "branch": "HCM",
             "position_name": "Nhóm phát triển",
             "deparment_name": "Phòng Dịch vụ gia tăng",
             "branch_name": "Chi nhánh Hồ Chí Minh",
             "dob": 1513651191000,
             "phone": "0961095661",
             "email": "leon.tran@mobistar.vn",
             "address": "Saigon Vietnam",
             "avatar": "https://cdn.mobistar.vn/18963.png"
          }
      }


.. _in-profile-update:

Update profile
--------------
.. http:post::  /api/v1/profile/set

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg phone: Điện thoại.
   :arg address: Địa chỉ.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "phone": "0961095661",
          "address": "Saigon Vietnam"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": ""
      }



.. _in-profile-change-pw:

Change password
---------------
.. http:post::  /api/v1/profile/change-password

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg current: Mật khẩu hiện tại (Đã mã hóa với :ref:`in-rule-secret-key`).
   :arg new: Mật khẩu mới (Đã mã hóa với :ref:`in-rule-secret-key`).

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "current": "_HASH_",
          "new": "_HASH_"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": ""
      }



.. _in-profile-reset-pw:

Reset password
--------------
.. http:post::  /api/v1/profile/reset-password

   :arg imei: IMEI của thiết bị (Đã mã hóa với :ref:`in-rule-secret-key`).
   :arg mac: Địa chỉ MAC của thiết bị (Đã mã hóa với :ref:`in-rule-secret-key`).
   :arg username: Tên người dùng (Đã mã hóa với :ref:`in-rule-secret-key`).
   :arg checksum: :ref:`in-rule-checksum`.

   .. sourcecode:: js

      {
          "imei": "356938035643809",
          "mac": "00:0a:95:9d:68:16",
          "username": "leon.tran@mobistar.vn",
          "checksum": "_HASH_"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": ""
      }


.. note:: Generate ra một mật khẩu mới và gửi mật khẩu này vào email của user_id trên.

.. _in-profile-permission:

Get permission
--------------
.. http:post::  /api/v1/profile/permission

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
   :>json object data: Các tính năng được phép.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "data":
          [
             {"code":"CODE1", "name":"NAME1", "insert":1, "update":1, "delete":1},
             {"code":"CODE2", "name":"NAME2", "insert":1, "update":1, "delete":1},
             {"code":"CODE3", "name":"NAME3", "insert":1, "update":1, "delete":1}
          ]
      }



.. _in-profile-shift:

Get shift
--------------
.. http:post::  /api/v1/profile/shift

   :arg access_token: Xem :ref:`in-get-token`.
   :arg checksum: :ref:`in-rule-checksum`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg from_date: Lấy dữ liệu từ ngày.
   :arg to_date: Lấy dữ liệu đến ngày.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "from_date": "2017-11-01",
          "to_date": "2017-11-30"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json object data: Những ca làm việc của nhân viên này.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "data":
          {
             "day":
             {
             	"name":"Hanh Chinh",
             	"time_in":"8:00",
             	"start_rest":"12:00",
             	"end_rest":"13:30",
             	"time_out":"17:30"
             }
          }
      }



OAuth
=====

Tài liệu này mô tả cách Ứng dụng lấy Access Token Key từ WebService. Bao gồm 2 bước sau:

* :ref:`in-req-token`
* :ref:`in-get-token`

.. _in-req-token:

Request Token Code
------------------
.. http:post::  /api/v1/oauth/request

   :arg imei: IMEI của thiết bị (Đã mã hóa với :ref:`in-rule-secret-key`).
   :arg mac: Địa chỉ MAC của thiết bị (Đã mã hóa với :ref:`in-rule-secret-key`).
   :arg username: Tên người dùng (Đã mã hóa với :ref:`in-rule-secret-key`).
   :arg password: Mật khẩu (Đã mã hóa với :ref:`in-rule-secret-key`).
   :arg checksum: :ref:`in-rule-checksum`.

   .. sourcecode:: js

      {
          "imei": "356938035643809",
          "mac": "00:0a:95:9d:68:16",
          "username": "leon.tran@mobistar.vn",
          "password": "_",
          "checksum": "_HASH_"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json object data: :ref:`in-rule-data-access-code`.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "data":
          {
             "access_code": "_HASH_",
             "expires_in": 30
          }
      }

.. _in-get-token:

Get Access Token Key
--------------------
.. http:post::  /api/v1/oauth/get

   :arg imei: IMEI của thiết bị (Đã mã hóa với :ref:`in-rule-secret-key`).
   :arg mac: Địa chỉ MAC của thiết bị (Đã mã hóa với :ref:`in-rule-secret-key`).
   :arg access_code: Xem :ref:`in-req-token`.

   .. sourcecode:: js

      {
          "imei": "356938035643809",
          "mac": "00:0a:95:9d:68:16",
          "access_code": "_HASH_"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json object data: :ref:`in-rule-data-access-token`.
   :>json integer current_time: Ngày và Giờ hiện tại của Server.

   .. sourcecode:: js

      {
          "error_code": 0,
          "error_message": "",
          "data":
          {
             "user_id": "18963",
             "access_token": "_HASH_",
             "expiration": 1513651191000,
             "current_time": 1513651191000
          }
      }



Employee Profile
================

Tài liệu này mô tả cách sử dụng thông tin người dùng từ WebService. Bao gồm các phần sau:

* :ref:`in-profile-get`
* :ref:`in-profile-update`

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



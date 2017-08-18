Employee Profile
================

Tài liệu này mô tả cách sử dụng thông tin người dùng từ WebService. Bao gồm các phần sau:

* :ref:`in-profile-get`
* :ref:`in-profile-update`

.. _in-profile-get:

Get profile
------------------
.. http:post::  /api/v1/profile/get

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
   :>json string user_id: ID định danh.
   :>json string fullname: Họ và tên.
   :>json string position: Vị trí.
   :>json string deparment: Bộ phận.
   :>json string branch: Chi nhánh.
   :>json string dob: Ngày sinh.
   :>json string phone: Điện thoại.
   :>json string email: Thư điện tử.
   :>json string avatar: Đường dẫn ảnh.

   .. sourcecode:: js

      {
          "status": true,
          "user_id": "18963",
          "fullname": "Leon Tran",
          "position": "DEV",
          "deparment": "VAS",
          "branch": "HCM",
          "dob": "1993-09-19",
          "phone": "0961095661",
          "email": "leon.tran@mobistar.vn",
          "avatar": "https://cdn.mobiistar.vn/18963.png" 
      }

   


.. _in-profile-update:

Update profile
--------------------
.. http:post::  /api/v1/profile/set

   :arg access_token: Xem :ref:`in-get-token`.
   :arg user_id: ID người dùng.
   :arg client_id: ID client.
   :arg fullname: Họ và tên.
   :arg email: Email.
   :arg phone: Điện thoại.
   :arg address: Địa chỉ.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "user_id": "18963",
          "client_id": "18963",
          "fullname": "Leon Tran",
          "email": "leon.tran@mobistar.vn",
          "phone": "0961095661",
          "address": "Saigon Vietnam"
      }


   :>json boolean status: :ref:`in-rule-res-status`.

   .. sourcecode:: js

      {
          "status": true
      }



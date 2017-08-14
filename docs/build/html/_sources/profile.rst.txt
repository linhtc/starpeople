Employee Profile
================

Tài liệu này mô tả cách sử dụng thông tin người dùng từ WebService. Bao gồm các phần sau:

* :ref:`in-profile-get`
* :ref:`in-profile-update`

.. _in-profile-get:

Get profile
------------------
.. http:post::  /api/v1/profile/get

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.

   .. sourcecode:: js

      {
          "access_token": "_HASH_"
      }


   :>json boolean status: Trạng thái xử lý của Server.
   :>json integer user_id: ID định danh.
   :>json string fullname: Họ và tên.
   :>json string deparment: Bộ phận.
   :>json string email: Thư điện tử.
   :>json string phone: Điện thoại.
   :>json string cmnd: Chứng minh thư, hộ chiếu.
   :>json string address: Chỗ ở hiện tại.
   :>json string avatar: Đường dẫn ảnh.


.. _in-profile-update:

Update profile
--------------------
.. http:post::  /api/v1/profile/set

   :arg access_token: Access Token Key lấy được ở bước :ref:`in-get-token`.
   :arg fullname: Họ và tên.
   :arg email: Email.
   :arg phone: Điện thoại.
   :arg address: Địa chỉ.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "fullname": "Leon Tran",
          "email": "leon.tran@mobistar.vn",
          "phone": "0961095661",
          "address": "Saigon Vietnam"
      }


   :>json boolean status: Trạng thái xử lý của Server.

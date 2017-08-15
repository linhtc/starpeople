OAuth
===============

Tài liệu này mô tả cách Ứng dụng lấy Access Token Key từ WebService. Bao gồm 2 bước sau:

* :ref:`in-req-token`
* :ref:`in-get-token`

.. _in-req-token:

Request Token Code
------------------
.. http:post::  /api/v1/oauth/request

   :arg imei: IMEI của thiết bị.
   :arg mac: Địa chỉ MAC của thiết bị.
   :arg username: Tên người dùng.
   :arg password: Mật khẩu.

   .. sourcecode:: js

      {
          "imei": "356938035643809", 
          "mac": "00:0a:95:9d:68:16", 
          "username": "leon.tran@mobiistar.vn", 
          "password": "_HASH_" 
      }


   :>json boolean status: :ref:`in-rule-res-status`.
   :>json string token_code: Token code Server cấp phát.


.. _in-get-token:

Get Access Token Key
--------------------
.. http:post::  /api/v1/oauth/get

   :arg token_code: Xem :ref:`in-req-token`.

   .. sourcecode:: js

      {
          "token_code": "_HASH_"
      }


   :>json string user_id: ID định danh.
   :>json string access_token: Access Token Key.
   :>json string expiration: Thời gian hết hiệu lực type ("Y-m-d H:i:s").

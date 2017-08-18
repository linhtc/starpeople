Salary Information
==================

Tài liệu này mô tả cách xem thông tin lương từ WebService. Bao gồm các phần sau:

* :ref:`in-salary-get`
* :ref:`in-salary-extra`

.. _in-salary-get:

Get salary
----------
.. http:post::  /api/v1/salary/get

   :arg access_token: Xem :ref:`in-get-token`.
   :arg month: Phiếu lương tháng [1-12]

   .. sourcecode:: js

      {
          "access_token": "_HASH_", 
          "month": "1"
      }


   :>json boolean status: :ref:`in-rule-res-status`.
   :>json string fullname: Họ và tên.
   :>json string position: Vị trí.
   :>json string deparment: Bộ phận.
   :>json string branch: Chi nhánh.
   :>json float salary: Lương thực lĩnh.

   .. sourcecode:: js

      {
          "status": true,
          "fullname": "Leon Tran",
          "position": "DEV",
          "deparment": "VAS",
          "branch": "HCM",
          "salary": 1234.0
      }

   


.. _in-salary-extra:

Extra salary
--------------------
.. http:post::  /api/v1/salary/extra

   :arg access_token: Xem :ref:`in-get-token`.
   :arg deal: Mức yêu cầu cộng thêm.
   :arg reason: Lý do.

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "deal": "50.000",
          "reason": "Thiếu 50k nữa mới được vào Casino"
      }


   :>json boolean status: :ref:`in-rule-res-status`.

   .. sourcecode:: js

      {
          "status": true
      }

   

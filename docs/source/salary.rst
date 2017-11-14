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
   :arg checksum: :ref:`in-rule-checksum`.
   :arg month: Phiếu lương tháng [1-12]

   .. sourcecode:: js

      {
          "access_token": "_HASH_",
          "checksum": "_HASH_",
          "month": "1"
      }


   :>json integer error_code: :ref:`in-rule-error-code`.
   :>json string error_message: :ref:`in-rule-error-message`.
   :>json object data: :ref:`in-rule-data-salary`.

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
             "salary": 1234.0
          }
      }

   


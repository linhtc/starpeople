General Rules
=============

Phần này mô tả các quy định theo chuẩn RESTful, các biến và giá trị mặc định cần thiết.

.. note:: Tài liệu đang trong quá trình hoàn thiện và chỉnh sửa cho phù hợp.
          Những nội dung được mô tả chưa khái quát hết chức năng của ứng dụng nên cần thảo luận thêm.
          Mọi phản hồi về sai sót cũng như góp ý xin liên hệ VAS Team: labs.mobiistar@gmail.com.
          Chân thành cảm ơn!
          
.. _in-rule-res-header:

Response header
---------------
Response header phải là kiểu JSON::

    {"integer":1, "boolean":true, "string":"^_^", "array": []}

.. _in-rule-res-status:

Response status
---------------
Trong JSON object trả về luôn có key status quy định trạng thái xử lý của Server.
Là một biến kiểu ``boolean`` với hai giá trị:

* true - Server hoàn thành việc xử lý.
* false - Server hoàn thành việc xử lý kèm cảnh báo.

Nếu ``false`` thì thiết bị sẽ tìm thêm key ``message`` để xác định tình trạng:

.. code-block:: restructuredtext

    # True
    .. response:: 
        :status: true

    # False
    .. response:: 
        :status: false
        :message: Something wrong ;((

.. _in-rule-kind-mapping:

Kind definition
---------------
Là một biến kiểu ``integer`` xác định loại phép.

* 0 - Nghỉ phép năm.
* 1 - Nghỉ thai sản.
* 2 - Nghỉ phép không lương.

.. _in-rule-approval-mapping:

Approval definition
-------------------
Là một biến kiểu ``integer`` xác định trạng thái duyệt đơn nghỉ phép, tăng ca.

* 0 - Không duyệt.
* 1 - Đồng ý.
* 2 - Yêu cầu chỉnh sửa.

.. _in-rule-secret-key:

Secret Key
----------
Là mã bảo được dùng để mã hóa và giải mã giữa client/server.

.. _in-rule-checksum:

Check Sum
---------
Theo cách sau:

.. code-block:: js

    checksum ( hash_256 [imei, mac, username, password], key)

Trong đó imei, mac, username, password đã được mã hóa với key (:ref:`in-rule-secret-key`).

.. _in-rule-error-code:

Error Code
----------
Là một biến kiểu ``integer`` xác định lỗi.

* 0 - Không có lỗi.
* 1 - Mã lỗi ứng với "CODE 1".
* 2 - Mã lỗi ứng với "CODE 2".
* 3 - ...

.. _in-rule-error-message:

Error Message
-------------
Mô tả lỗi đi kèm với :ref:`in-rule-error-code`.

.. _in-rule-data-access-code:

Access Code Data
----------------
Là một JSON ``object`` nhận được khi :ref:`in-req-token`. Bao gồm:

* **access_code** (*string*) - Code để :ref:`in-get-token`.
* **expires_in** (*integer*) - Thời gian hết hạn được tính bằng giây.

.. sourcecode:: js

      {
          "access_code": "_HASH_",
          "expires_in": 30
      }


.. _in-rule-data-access-token:

Access Token Data
-----------------
Là một JSON ``object`` nhận được khi :ref:`in-get-token`. Bao gồm:

* **user_id** (*string*) - ID định danh người dùng.
* **access_token** (*string*) - Access Token Key.
* **expires_time** (*long*) - Thời gian hết hạn (Unix timestamp).

.. sourcecode:: js

      {
          "user_id": "18963",
          "access_token": "_HASH_",
          "expiration": 1513651191000
      }


.. _in-rule-data-profile:

Profile Data
------------
Là một JSON ``object`` nhận được khi :ref:`in-profile-get`. Bao gồm:

* **user_id** (*string*) - ID định danh người dùng.
* **fullname** (*string*) - Họ và tên.
* **position** (*string*) - Vị trí.
* **deparment** (*string*) - Bộ phận.
* **branch** (*string*) - Chi nhánh.
* **dob** (*long*) - Ngày sinh.
* **phone** (*string*) - Điện thoại.
* **email** (*string*) - Thư điện tử.
* **avatar** (*string*) - Đường dẫn ảnh.

.. sourcecode:: js

      {
          "user_id": "18963",
          "fullname": "Leon Tran",
          "position": "DEV",
          "deparment": "VAS",
          "branch": "HCM",
          "dob": 1513651191000,
          "phone": "0961095661",
          "email": "leon.tran@mobistar.vn",
          "avatar": "https://cdn.mobistar.vn/18963.png"
      }


.. _in-rule-data-absent:

Absent Data
-----------
Là một JSON ``object`` nhận được khi :ref:`in-work-absence-detail`. Bao gồm:

* **user_id** (*string*) - ID định danh người dùng.
* **fullname** (*string*) - Họ và tên.
* **position** (*string*) - Vị trí.
* **deparment** (*string*) - Bộ phận.
* **branch** (*string*) - Chi nhánh.
* **phone** (*string*) - Điện thoại.
* **email** (*string*) - Thư điện tử.
* **absent_time** (*arrray*) - Thời gian nghỉ [1513651191000, 1513651191000].
* **kind** (*integer*) - Loại phép (Xem :ref:`in-rule-kind-mapping`).
* **reason** (*string*) - Lý do.

.. sourcecode:: js

      {
          "user_id": "18963",
          "fullname": "Leon Tran",
          "position": "DEV",
          "deparment": "VAS",
          "branch": "HCM",
          "phone": "0961095661",
          "email": "leon.tran@mobistar.vn",
          "absent_time": [1513651191000, 1513651191000],
          "kind": 0,
          "reason": "Sick"
      }


.. _in-rule-data-overtime:

Overtime Data
-------------
Là một JSON ``object`` nhận được khi :ref:`in-work-overtime-detail`. Bao gồm:

* **user_id** (*string*) - ID định danh người dùng.
* **fullname** (*string*) - Họ và tên.
* **position** (*string*) - Vị trí.
* **deparment** (*string*) - Bộ phận.
* **branch** (*string*) - Chi nhánh.
* **phone** (*string*) - Điện thoại.
* **email** (*string*) - Thư điện tử.
* **absent_time** (*arrray*) - Thời gian nghỉ [1513651191000, 1513651191000].
* **reason** (*string*) - Lý do.

.. sourcecode:: js

      {
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


.. _in-rule-data-salary:

Salary Data
-------------
Là một JSON ``object`` nhận được khi :ref:`in-salary-get`. Bao gồm:

* **user_id** (*string*) - ID định danh người dùng.
* **fullname** (*string*) - Họ và tên.
* **position** (*string*) - Vị trí.
* **deparment** (*string*) - Bộ phận.
* **branch** (*string*) - Chi nhánh.
* **salary** (*float*) - Lương thực lĩnh.

.. sourcecode:: js

      {
          "user_id": "18963",
          "fullname": "Leon Tran",
          "position": "DEV",
          "deparment": "VAS",
          "branch": "HCM",
          "salary": 1234.0
      }



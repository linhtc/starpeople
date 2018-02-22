Upgrade table
=============

Phần này liệt kê những APIs nào đã được thay đổi hoặc thêm vào.

.. note:: Các phần được cập nhật trong version latest (1.0.4) ngày 29/01/2018.

+-----+------------------------------------------+----------------------------------------------+
| STT | APIs                                     | Description                                  |
+-----+------------------------------------------+----------------------------------------------+
| 1   | :ref:`in-work-timekeeping-check-in`      | ``update`` Them anh chup nhan vien           |
+-----+------------------------------------------+----------------------------------------------+
| 2   | :ref:`in-work-timekeeping-check-out`     | ``update`` Them anh chup nhan vien           |
+-----+------------------------------------------+----------------------------------------------+

Hai APIs trên mới được cập nhật lại nhằm tăng dữ liệu để kiểm tra, 
đối chiếu cho việc chấm công (Thêm phần ảnh chụp nhân viên)

-> Trên website cần thêm tính năng hiển thị ảnh chụp để người Quản lý có thể vào kiểm tra.

.. note:: Các phần được cập nhật trong version latest (1.0.3) ngày 14/12/2017.

+-----+------------------------------------------+----------------------------------------------+
| STT | APIs                                     | Description                                  |
+-----+------------------------------------------+----------------------------------------------+
| 1   | :ref:`in-work-update-application-absence`| ``new`` Cap nhat don duoc YC chinh sua       |
+-----+------------------------------------------+----------------------------------------------+
| 2   | :ref:`in-work-update-application-ot`     | ``new`` Cap nhat don duoc YC chinh sua       |
+-----+------------------------------------------+----------------------------------------------+
| 3   | :ref:`in-work-absence-table`             | ``update`` Them total time va hidden status  |
+-----+------------------------------------------+----------------------------------------------+
| 4   | :ref:`in-work-absence-employee-table`    | ``update`` Them total time va hidden status  |
+-----+------------------------------------------+----------------------------------------------+
| 5   | :ref:`in-work-absence-detail`            | ``update`` Them total time va hidden status  |
+-----+------------------------------------------+----------------------------------------------+
| 6   | :ref:`in-work-overtime-table`            | ``update`` Them total time va hidden status  |
+-----+------------------------------------------+----------------------------------------------+
| 7   | :ref:`in-work-overtime-employee-table`   | ``update`` Them total time va hidden status  |
+-----+------------------------------------------+----------------------------------------------+
| 8   | :ref:`in-work-overtime-detail`           | ``update`` Them total time va hidden status  |
+-----+------------------------------------------+----------------------------------------------+
| 9   | :ref:`in-profile-reset-pw`               | ``update`` Remove access_token               |
+-----+------------------------------------------+----------------------------------------------+
| 10  | :ref:`in-get-token`                      | ``update`` Them current time vao response    |
+-----+------------------------------------------+----------------------------------------------+

:ref:`in-work-update-application-absence`
-----------------------------------------

API này mới được thêm vào để những đơn có trạng thái Yêu cầu chỉnh sửa có thể cập nhật được.

:ref:`in-work-update-application-ot`
------------------------------------

API này mới được thêm vào để những đơn có trạng thái Yêu cầu chỉnh sửa có thể cập nhật được.

``#3 - #5`` là những APIs của phần Xin nghỉ phép có một vài thay đổi nhỏ sau:

* Thêm key **total_time** ở response để xác định số tổng ngày nghỉ phép.
* Trạng thái **hidden** thì không trả về trong response (trạng thái xóa trên web hoặc client cập nhật hidden = 1).

``#6 - #8`` là những APIs của phần Xin tăng ca có một thay đổi nhỏ sau:

* Trạng thái **hidden** thì không trả về trong response (trạng thái xóa trên web hoặc client cập nhật hidden = 1).

:ref:`in-profile-reset-pw`
--------------------------

API reset mật khẩu được thực hiện bên ngoài phạm vi đăng nhập nên không thể :ref:`in-get-token`.

:ref:`in-get-token`
--------------------------

API này đã có trước đó và được cập nhật lại các phần sau:

* **current_time** (*integer*) - Thêm current_time key trong Response.


.. note:: Các phần được cập nhật trong version latest (1.0.2) ngày 30/11/2017.
 
+-----+------------------------------------------+----------------------------------------------+
| STT | APIs                                     | Description                                  |
+-----+------------------------------------------+----------------------------------------------+
| 1   | :ref:`in-work-absence-employee-table`    | ``new`` Lay danh sach nhan vien xin nghi phep|
+-----+------------------------------------------+----------------------------------------------+
| 2   | :ref:`in-work-overtime-employee-table`   | ``new`` Lay danh sach nhan vien xin tang ca  |
+-----+------------------------------------------+----------------------------------------------+

:ref:`in-work-absence-employee-table`
-------------------------------------

API này mới được thêm vào để người quản lý lấy danh sách nhân viên xin nghỉ phép.

:ref:`in-work-overtime-employee-table`
--------------------------------------

API này mới được thêm vào để người quản lý lấy danh sách nhân viên xin tăng ca.


.. note:: Các phần được cập nhật trong version latest (1.0.2) ngày 17/11/2017.
 
+-----+------------------------------------------+----------------------------------------------+
| STT | APIs                                     | Description                                  |
+-----+------------------------------------------+----------------------------------------------+
| 1   | :ref:`in-profile-permission`             | ``new`` Lay danh sach quyen                  |
+-----+------------------------------------------+----------------------------------------------+
| 2   | :ref:`in-profile-shift`                  | ``new`` Lay danh sach ca                     |
+-----+------------------------------------------+----------------------------------------------+
| 3   | :ref:`in-profile-get`                    | ``update`` Xem thong tin ca nhan             |
+-----+------------------------------------------+----------------------------------------------+
| 4   | :ref:`in-work-timekeeping-history`       | ``new`` Xem lich su cham cong                |
+-----+------------------------------------------+----------------------------------------------+
| 5   | :ref:`in-work-absence-table`             | ``update`` Lay danh sach xin nghi phep       |
+-----+------------------------------------------+----------------------------------------------+
| 6   | :ref:`in-work-overtime-table`            | ``update`` Lay danh sach xin tang ca         |
+-----+------------------------------------------+----------------------------------------------+
| 7   | :ref:`in-profile-change-pw`              | ``new`` Doi mat khau                         |
+-----+------------------------------------------+----------------------------------------------+
| 8   | :ref:`in-profile-reset-pw`               | ``new`` Reset mat khau                       |
+-----+------------------------------------------+----------------------------------------------+

:ref:`in-profile-permission`
----------------------------

API này mới được thêm vào nhằm lấy quyền truy cập vào các tính năng của ứng dụng.
Dữ liệu nhận về là một ``object`` có dạng:

.. sourcecode:: js

      [
         {"code":"CODE1", "name":"NAME1", "insert":1, "update":1, "delete":1},
         {"code":"CODE2", "name":"NAME2", "insert":1, "update":1, "delete":1},
         {"code":"CODE3", "name":"NAME3", "insert":1, "update":1, "delete":1}
      ]


:ref:`in-profile-shift`
-----------------------

API này mới được thêm vào nhằm lấy danh sách ca làm việc của một nhân viên.
Dữ liệu nhận về là một ``object`` có dạng:

.. sourcecode:: js

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


:ref:`in-profile-get`
-----------------------------

API này đã có trước đó và được cập nhật lại các phần sau:

* **address** (*string*) - Thêm address key trong Response.


:ref:`in-work-timekeeping-history`
----------------------------------

API này mới được thêm vào nhằm lấy lịch sử chấm công của nhân viên.
Dữ liệu nhận về là một ``array object`` có dạng:

.. sourcecode:: js

      [{
         "1513651191000": {
         	"in": {
         		"writen_time": 1513651191000,
         		"location": [10.785092, 106.6913373]
         	},
         	"out": {
         		"writen_time": 1513651191001,
         		"location": [10.785092, 106.6913373]
         	}
         }
      }]


:ref:`in-work-absence-table`
----------------------------

API này đã có trước đó và được cập nhật lại các phần sau:

* **from_date** (*date*) - Từ ngày.
* **to_date** (*date*) - Đến ngày.

:ref:`in-work-overtime-table`
-----------------------------

API này đã có trước đó và được cập nhật lại các phần sau:

* **user_id** (*string*) - Thêm ID định danh người dùng trong Request.
* **client_id** (*string*) - Thêm Client ID trong Request.
* **from_date** (*date*) - Từ ngày.
* **to_date** (*date*) - Đến ngày.


:ref:`in-profile-change-pw`
---------------------------

API này mới được thêm vào cho phép người dùng tự thay đổi mật khẩu đăng nhập.
Dữ liệu nhận về là một ``object`` có dạng:

.. sourcecode:: js

      {
          "error_code": 0,
          "error_message": ""
      }

:ref:`in-profile-reset-pw`
--------------------------

API này mới được thêm vào cho phép người dùng không thể thay đổi mật khẩu mới (do quên, etc.).
**Mật khẩu reset** sẽ được gửi qua email của chính user đó.
Dữ liệu nhận về là một ``object`` có dạng:

.. sourcecode:: js

      {
          "error_code": 0,
          "error_message": ""
      }



.. note:: Các phần được cập nhật trong version 1.0.1.

Không có dữ liệu nào được thêm vào!

 
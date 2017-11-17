Upgrade table
=============

Phần này liệt kê những APIs nào đã được thay đổi hoặc thêm vào.

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
| 5   | :ref:`in-work-overtime-table`            | ``update`` Lay danh sach xin nghi phep       |
+-----+------------------------------------------+----------------------------------------------+
| 6   | :ref:`in-profile-change-pw`              | ``new`` Doi mat khau                         |
+-----+------------------------------------------+----------------------------------------------+
| 7   | :ref:`in-profile-reset-pw`               | ``new`` Reset mat khau                       |
+-----+------------------------------------------+----------------------------------------------+

:ref:`in-profile-permission`
----------------------------
API này mới được thêm vào nhằm lấy quyền truy cập vào các tính năng của ứng dụng.
Dữ liệu nhận về là một ``object`` có dạng:

.. sourcecode:: js

      {
         "profile": {"get":1, "update":1},
         "absence": {"apply":1, "confirm":0, "apply":1, "table":1, "management":1},
         "overtime": {"apply":1, "confirm":0, "apply":1, "table":1, "management":1},
         "salary": {"get":1}
      }


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



:ref:`in-work-overtime-table`
-----------------------------
API này đã có trước đó và được cập nhật lại các phần sau:

* **user_id** (*string*) - Thêm ID định danh người dùng trong Request.
* **client_id** (*string*) - Thêm Client ID trong Request.


.. note:: Các phần được cập nhật trong version 1.0.1.

Không có dữ liệu nào được thêm vào!
 
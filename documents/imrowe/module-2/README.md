
<div align="center">

<img src="https://img.shields.io/badge/PRACTICE-TASK%20v2.0-4f46e5?style=for-the-badge&labelColor=1f2937" alt="badge"/>

# 🗂️ Менеджер задач v 0.2.0

<em>Дорогие студенты — наша задача превратить работающее приложение в чистый модульный проект.</em>

<br/>

![status](https://img.shields.io/badge/view-contoller-10b981?style=flat-square)
![level](https://img.shields.io/badge/module-project-f59e0b?style=flat-square)
![stack](https://img.shields.io/badge/stack-python%20%7C%20tkinter-4f46e5?style=flat-square)

</div>

---

### 🎯 &nbsp;Цель

> Переработать приложение в **модульную архитектуру** из четырёх классов и реализовать полный CRUD с отделением логики от интерфейса.

---

### 🏗️ &nbsp;Классы

| &nbsp; | Класс | Ответственность |
|:--:|:--|:--|
| 1 | **`Task`** | Шаблон задачи: `id`, `title`, `description`, `status`, `author`, `created_at` |
| 2 | **`StorageManager`** | Сохранение (JSON): `load`, `save`, `add`, `update`, `delete` |
| 3 | **`Interface`** | Прослойка к `tkinter` через `AppButton`, `AppListbox`, `AppEntry`, `AppLabel` |
| 4 | **`TaskManager`** | Фасад: связывает всё вместе. `create_task`, `edit_task`, `delete_task`, `toggle_status`, `run` |

---

### 🪜 &nbsp;Порядок работы

1. **Класс `Task`** — опишите поля и методы `to_dict()` / `from_dict()`. Проверьте в консоли.
2. **Класс `StorageManager`** — реализуйте `load / save / add / update / delete`. Протестируйте без GUI.
3. **Компоненты `App*`** — создайте `AppButton`, `AppEntry`, `AppLabel`, `AppListbox` как наследников `tk`-виджетов.
4. **Класс `Interface`** — соберите фасад для `tkinter`: методы `build`, `get_input`, `clear_input`, `show_tasks`, `show_message`, `ask_confirm`.
5. **Класс `TaskManager`** — свяжите `Task`, `StorageManager` и `Interface`. Реализуйте `create_task`, `edit_task`, `delete_task`, `toggle_done`, `refresh`, `run`.
6. **`main.py`** — точка входа: создайте `TaskManager`, вызовите `run()`.
7. **Проверка** — создайте, измените, удалите задачи, закройте и откройте приложение — данные должны сохраниться.

---

> 💬 Заготовки с сигнатурами классов приложены отдельно — заполните их рабочим кодом.

---

### ✅ &nbsp;Требования

- [x] Создание, изменение, удаление задач и отметка «выполнено»
- [x] Сохранение / загрузка через `StorageManager`
- [x] UI **только** через компоненты `App*`, без «голого» tkinter в `TaskManager`
- [x] Валидация ввода и обработка ошибок

---


<div align="center">

💡 *Начните с `Task` и `StorageManager` — их можно проверить без GUI. Удачи!* 🚀

<br/>

![deadline](https://img.shields.io/badge/дедлайн-__09.11.26___-6b7280?style=flat-square)
![format](https://img.shields.io/badge/формат-zip%20%2B%20README-4f46e5?style=flat-square)

</div>

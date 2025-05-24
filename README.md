# 🧱 Toolbox Core

![Toolbox Badge](https://img.shields.io/badge/Toolbox-Core%20Kit-gray?style=flat-square&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.x-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

`toolbox-core` is the **foundation module** of the Toolbox Project. It centralizes shared assets and utilities like base templates, custom widgets, and template tags used across all other Toolbox apps.

---

## 📦 What’s Included?

### 🧩 Base Templates
- `base.html` and layout-ready blocks (`content`, `title`, `scripts`)
- Generic include templates for:
  - ✅ Form rendering
  - ✅ Pagination
  - ✅ Messages
- Built with Bootstrap 5 and template inheritance in mind

### 🎛️ Custom Widgets
- `customFileInput`: clearable file input with thumbnail preview
- `ReadOnlyTextWidget`: display data in uneditable form fields
- Easily pluggable in any form via standard widget override

### 🏷️ Template Tags
- Organized in `templatetags/custom_tags.py`
- Includes:
  - `setValidationClass`: adds Bootstrap `is-valid` / `is-invalid` classes
  - Custom filters and utilities for dynamic rendering

---

## 🔗 Designed to be Extensible

Other Toolbox apps like:

- `toolbox-auth-kit`
- `toolbox-image-kit`
- `toolbox-export-kit`

...extend templates, include components, and reuse helpers from this module to stay **DRY**, clean, and consistent.

---

## ✅ Best Practices

| Area               | Approach                                     |
|--------------------|----------------------------------------------|
| Templates          | App-scoped, inheritable via `core/base.html` |
| Widgets            | Defined in a dedicated `widgets.py`          |
| Template Tags      | Scoped under `custom_tags.py`                |
| Styling            | Uses Bootstrap classes by default            |
| Reusability        | Plug-and-play with any other Django app      |

---

## 📁 Suggested Structure

```
toolbox_core/
├── templates/
│   └── core/
│       ├── base.html
│       ├── includes/
│       │   ├── form_render.html
│       │   ├── alerts.html
│       │   └── pagination.html
├── widgets.py
├── templatetags/
│   └── custom_tags.py
```

---

## 🛠️ Usage Example

### Extending `base.html` from another app:

```django
{% extends "core/base.html" %}

{% block content %}
  <h2>My Page</h2>
{% endblock %}
```

### Using a template tag:

```django
<input type="text" name="email" class="{{ field|setValidationClass }}">
```

---

## 🧠 About Toolbox Project

> Toolbox is a modular ecosystem of Django-ready kits built to scale real-world applications efficiently.

`toolbox-core` is the **glue** that holds them together — think of it as the utility library for your web UI and form logic.

---

## 🤝 Credits

Thanks for following the development of Toolbox project on GitHub. Contributions and feedback are welcome to continue improving and scaling the platform.

---

> Built with Django ❤️
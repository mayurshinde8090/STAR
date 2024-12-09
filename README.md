# STAR
# STAR: Student TC and Admission Register

**STAR** is a software application designed to streamline the management of student admission records and transfer certificates (TC). It allows users to perform essential operations like inserting, updating, deleting, and searching records, both individually and collectively.

---

## Objectives
The primary objectives of the **STAR** project are:
1. To computerize the admission record management system.
2. To computerize the transfer certificate (TC) record management system.
3. To enable efficient updating of admission records.
4. To provide a robust search functionality for single and multiple records.

---

## Platform
The STAR project is built on the following platform:
- **Operating System**: Windows XP or higher
- **Programming Language**: Python
- **Data Storage**: MySQL

---

## Table Structure

### Table: `admn` (Admission Records)
| Sr. No | Field Name   | Datatype | Size | Remark       |
|--------|--------------|----------|------|--------------|
| 1      | `Admn_no`    | Int      | 6    | Primary Key  |
| 2      | `Dateofadmn` | Varchar  | 10   |              |
| 3      | `Name`       | Char     | 30   |              |
| 4      | `Father_name`| Char     | 30   |              |
| 5      | `Mother_name`| Char     | 30   |              |
| 6      | `DOB`        | Varchar  | 10   |              |
| 7      | `Admn_Cat`   | Varchar  | 3    |              |
| 8      | `Class`      | Varchar  | 4    |              |
| 9      | `Caste`      | Char     | 10   |              |
| 10     | `TC_no`      | Int      | 10   |              |
| 11     | `TC_date`    | Varchar  | 10   |              |

### Table: `tc` (Transfer Certificate Records)
| Sr. No | Field Name   | Datatype | Size | Remark       |
|--------|--------------|----------|------|--------------|
| 1      | `TC_no`      | Int      | 10   | Primary Key  |
| 2      | `TC_date`    | Varchar  | 10   |              |
| 3      | `Admn_no`    | Int      | 6    | Foreign Key  |
| 4      | `Name`       | Char     | 30   |              |
| 5      | `Reason`     | Char     | 30   |              |
| 6      | `Remark`     | Char     | 100  |              |

---

## Features

### Operations on `admn` Table
1. **Insert** Student Details.
2. **Update** Student Details.
3. **Delete** Student Details.
4. **Search** Individual Student Details.
5. **Search All** Student Details.
6. **Exit**.

### Operations on `tc` Table
1. **Insert** TC Details.
2. **Update** TC Details.
3. **Delete** TC Details.
4. **Search** Individual TC Details.
5. **Search All** TC Details.
6. **Exit**.



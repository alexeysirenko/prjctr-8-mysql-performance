# prjctr-8-mysql-performance

# Performance Test Results

## Query: `SELECT COUNT(*) FROM testdb.users WHERE dob = '1950-01-01'`

- **Records**: 2187

| Index Type | Elapsed Time                                                                                                                        |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| No Index   | 8s                                                                                                                                  |
| BTREE      | 0.003s                                                                                                                              |
| Hash       | MySQL does not allow creating hash indexes with date columns and InnoDB engine. Index will be created, but it will have BTREE type. |

---

## Query: `SELECT COUNT(*) FROM testdb.users WHERE dob BETWEEN '1950-01-01' AND '1950-03-01'`

- **Records**: 131598

| Index Type | Elapsed Time                                                                                                                        |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| No Index   | 18s                                                                                                                                 |
| BTREE      | 0.071s                                                                                                                              |
| Hash       | MySQL does not allow creating hash indexes with date columns and InnoDB engine. Index will be created, but it will have BTREE type. |

---

## Insert Tests

### Insert Random 1M Users (Batch Size: 100k)

| `innodb_flush_log_at_trx_commit` | Index Type | Elapsed Time |
| -------------------------------- | ---------- | ------------ |
| 1 (default)                      | BTREE      | 29s          |
|                                  | None       | 13.7s        |
| 0                                | BTREE      | 28s          |
|                                  | None       | 13s          |
| 2                                | BTREE      | 37s          |
|                                  | None       | 13s          |

---

### Insert Random 100,000 Users (Batch Size: 100)

| `innodb_flush_log_at_trx_commit` | Index Type | Elapsed Time |
| -------------------------------- | ---------- | ------------ |
| 1 (default)                      | BTREE      | 23s          |
| 0                                | BTREE      | 8.7s         |
| 2                                | BTREE      | 8.8s         |

---


## Siege Tests

### Siege Command:

- `siege -c10 -r3 -f urls.txt` (Insert Random 50 Users, Batch Size: 1, 10 parallel API users)

| `innodb_flush_log_at_trx_commit` | Elapsed Time | Response Time | Longest Transaction |
| -------------------------------- | ------------ | ------------- | ------------------- |
| 1                                | 34.93s       | 11.51s        | 12.09s              |
| 0                                | 17.82s       | 5.87s         | 6.27s               |
| 2                                | 18.21s       | 5.99s         | 6.69s               |

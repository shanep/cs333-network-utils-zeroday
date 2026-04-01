# CS333 — Packet Builder Class Activity

NAME: ___________________________

NAME: ___________________________

NAME: ___________________________

**Duration:** ~45 minutes
**Format:** Pairs or individual
**Tool:** `uv run main.py` in this repo

---

## Quick Reference

| `struct` format char | Width (bytes) | Meaning                         |
| -------------------- | ------------- | ------------------------------- |
| `B`                  | 1             | unsigned byte                   |
| `H`                  | 2             | unsigned short (16-bit)         |
| `I`                  | 4             | unsigned int (32-bit)           |
| `4s`                 | 4             | 4-byte string                   |
| `!`                  | —             | network (big-endian) byte order |

---

## Learning Objectives

By the end of this activity you should be able to:
- Read and decode binary protocol headers using Python's `struct` module
- Explain how the IPv4 checksum algorithm works at a high level
- Reconstruct the TCP three-way handshake using flags and sequence numbers
- Trace how packet bytes map to protocol fields

---

## Part 1 — Reading the Code (10 min)

Open [main.py](main.py) and answer the following questions **without running the tool yet.**

### Q1. Struct format strings

The IPv4 header is packed with this struct format (line 109):

```python
STRUCT: ClassVar[struct.Struct] = struct.Struct("!BBHHHBBH4s4s")
```

Fill in the table using the Quick Reference above. The first two rows are done for you.

| Format char | Width (bytes) | Field name in `IPv4Header` |
| ----------- | ------------- | -------------------------- |
| `!`         | —             | *(byte order)*             |
| `B`         | 1             | `version_ihl`              |
| `B`         | 1             | `dscp_ecn`                 |
| `H`         | 2             | `total_length`             |
| `H`         |               |                            |
| `H`         |               |                            |
| `B`         |               |                            |
| `B`         |               |                            |
| `H`         |               |                            |
| `4s`        |               |                            |
| `4s`        |               |                            |

**Total bytes =** _______ (does this match `SIZE = 20`?)

---

### Q2. TCP flags bitmask

The `data_off_flags` field packs the 4-bit data offset and the 9 TCP flags into one `uint16`.

```python
FLAG_SYN: ClassVar[int] = 0x002
FLAG_ACK: ClassVar[int] = 0x010
```

What is the value of `data_off_flags` for a SYN-ACK packet whose data offset is 5 (20-byte header)?

Step-by-step:
- Data offset 5 in top 4 bits: `5 << 12` = `0x5000`
- SYN flag: `0x002`
- ACK flag: `0x010`
- OR them together: `0x5000 | 0x002 | 0x010` = **`0x____`**

---

## Part 2 — Hands-on Packet Building (20 min)

Run the commands below and record the output. Answer each question before moving to the next command.

---

### Exercise A — Ethernet + IPv4 basics

```bash
uv run main.py create --preset ping --dst-ip 10.0.0.1 --output ping.pkt
uv run main.py read ping.pkt --hexdump
```

1. What are the src and dst MAC addresses shown in the output? Why are they placeholder values (`aa:bb:cc:dd:ee:ff`) instead of real hardware addresses?

2. The ICMP Echo Request is **type 8**. What byte offset from the start of the Ethernet frame does the ICMP type field appear at?
   - Ethernet header = 14 bytes
   - IPv4 header = 20 bytes
   - ICMP type = first byte of ICMP header
   - **Byte offset =** 14 + 20 + 0 = _______

3. What is the total `frame length` printed by `read`? Break it down:
   - Ethernet: 14 B
   - IPv4: 20 B
   - ICMP: 8 B
   - Payload: ______ B
   - **Total:** ______ B

---

## Wrap-up Discussion (5 min)

1. What surprised you about building packets byte-by-byte with `struct`? How does this compare to using a high-level library?

2. The `send` command uses a raw socket (`socket.IPPROTO_RAW`). What does this allow you to do with the source IP address, and why is that a concern?

3. When would you use UDP instead of TCP for a protocol you were designing? What trade-offs does the DNS exercise illustrate?

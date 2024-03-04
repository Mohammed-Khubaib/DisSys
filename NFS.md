## Program: Learning About and Setting Up NFS

**Aim:** Understand how Network File System (NFS) works and set it up.

**Description:** NFS lets computers share files over a network. Servers share files, and clients access them. We'll learn to set up NFS on both the server and client sides.

**Steps:**

1. **Study NFS:**
   - Make a folder called "nfs" and put a file "abc.txt" inside.
   - Find the server's IP address.

2. **Enable necessary services:**
   - Turn on Network and NFS services.
   - Make sure the firewall and security settings allow NFS.

3. **Set up NFS Server:**
   - Configure NFS settings with low security.
   - Restart NFS service in the Terminal.

4. **Configure NFS Client:**
   - Use Terminal to check disk space and mount the NFS share.
   - Access files in the shared directory.
   - When done, unmount the NFS share.

**Note:** If network isn't working, restart it using "service network restart".
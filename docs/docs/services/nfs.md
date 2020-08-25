# NFS

Please refer to [ubunut-help](https://help.ubuntu.com/community/NFSv4Howto) to
see how NFSv4 works. Make sure to mount the directories you want to export
inside the */export* folder of the NFS container. Mount them with the `:ro`
option if you want them to be read-only (and configure them in the **exports**
conf accordingly).

## Ports

* **2049/tcp**.

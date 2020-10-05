#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

#include <linux/fs.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <linux/mm.h>
#include <linux/swap.h>

#include <linux/vmstat.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("S. Otzoy");
MODULE_DESCRIPTION("Modulo para obtener el uso de RAM");
MODULE_VERSION("0.01");

static int my_proc_show(struct seq_file *m, void *v) {
    struct sysinfo i;

    si_meminfo(&i);
    si_swapinfo(&i);

    long cached = global_node_page_state(NR_FILE_PAGES) - total_swapcache_pages() - i.bufferram;
    
    if (cached < 0){
        cached = 0;
    }

	seq_printf(m, "%lu\n%lu\n%lu\n%ld", i.totalram, i.freeram, i.bufferram, cached);
	return 0;
}

static ssize_t my_proc_write(struct file *file, const char __user *buffer, size_t count, loff_t *f_pos) {
	return 0;
}

static int my_proc_open(struct inode *inode, struct file *file)
{
	return single_open(file, my_proc_show, NULL);
}

static struct file_operations my_fops = {
	.owner = THIS_MODULE,
	.open = my_proc_open,
	.release = single_release,
	.read = seq_read,
	.llseek = seq_lseek,
	.write = my_proc_write
};

static int __init rammod_init(void) {
	struct proc_dir_entry *entry = proc_create("rammod", 0777, NULL, &my_fops);
	if (!entry){
		return -1;
	} else {
		printk(KERN_INFO "Rammod init\n");
	}
	return 0;
}

static void __exit rammod_exit(void) {
	remove_proc_entry("rammod", NULL);
	printk(KERN_INFO "Final\n");
} 

module_init(rammod_init);
module_exit(rammod_exit);
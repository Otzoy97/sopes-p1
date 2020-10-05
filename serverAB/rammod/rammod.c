#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

#include <linux/fs.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <linux/mm.h>
#include <linux/mmzone.h>
#include <linux/swap.h>
#include <linux/swapops.h>

#include <linux/kernel_stat.h>
#include <linux/list.h>
#include <linux/blkdev.h> 
#include <linux/cpumask.h> 


#include <asm/page.h>
#include <asm/pgtable.h>

#define CUATRO 4

MODULE_LICENSE("GPL");
MODULE_AUTHOR("S. Otzoy");
MODULE_DESCRIPTION("Modulo para obtener el uso de RAM");
MODULE_VERSION("0.21");

static int my_proc_show(struct seq_file *m, void *v) {
	long cached;
	struct sysinfo info;

	si_meminfo(&info);

	cached = global_node_page_state(NR_FILE_PAGES) - total_swapcache_pages() -info.bufferram;

	if (cached < 0)
		cached = 0;

	// unsigned long total, free, buffer, cached;
	// unsigned long fpags;
	// unsigned long swapcachepags;
	// int i;
	// struct list_head *all_bdevs;
	// struct address_space *my_swapper_spaces;
	// struct zone *zone;
	// *my_swapper_spaces = (struct address_space *)0xffffffff81c3b440;
	// all_bdevs; = (struct list_head *)0xffffffff81c3f540;

	// //Memoria-total
	// total = totalram_pages*CUATRO;
	// //Memoria-free
	// free = (*((unsigned long *)vm_stat+NR_FREE_PAGES))*4;
	// //Memoria-buffer
	// buffer = 0;
	// struct block_device *dv;
	// list_for_each_entry(dv, all_bdevs, bd_list) {
	// 	buffer += dv->bd_inode->i_mapping->nrpages;
	// }
	// buffer *= 4;
	// //Memoria-cache
	// fpags = *((unsigned long *)vm_stat+NR_FILE_PAGES);
	// swapcachepags = 0;
	// for (i = 0; i < MAX_SWAPFILES; i++){
	// 	swapcachepags += my_swapper_spaces[i].nrpages;
	// }
	// cached = (fpags-swapcachepags)*4-buffer;

	seq_printf(m, "%lu\n%lu\n%lu\n%lu", info.totalram << (PAGE_SHIFT - 10), info.freeram, info.bufferram, cached);
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
